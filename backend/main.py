from fastapi import FastAPI, Request
import joblib as jb
import pandas as pd
from base_dict_2 import base_dict
from meaning import getMeaning
import shap
import matplotlib.pyplot as plt
import io
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = jb.load("edpmodel.pkl")
le = jb.load("edple.pkl")

explainer = shap.TreeExplainer(model)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Early Disease Prediction API","ack":1}

@app.get("/symptoms")
def get_symptoms():
    symptoms = list(base_dict().keys())
    return {"symptoms": symptoms,"ack":1}

@app.post("/predict")
async def predict_disease(request: Request):
    try:
        body = await request.json()
        symptoms = body.get("input", [])

        inp = base_dict() #Fetching input base

        #-----INPUT--------
        for s in symptoms:
            if s in inp:
                inp[s] = 1
        input_df = pd.DataFrame([inp])
        #------------------

        probs = model.predict_proba(input_df)[0] #Prediction 

        #--------Probabilities and Top 5 Diseases--------
        top_indices = probs.argsort()[::-1][:5]
        top_diseases = le.inverse_transform(top_indices)

        prob_dict ={}
        for i, idx in enumerate(top_indices):
            disease = le.inverse_transform([idx])[0]
            prob_dict[disease] = float(probs[idx])
        #------------------------------------------------

        y_pred = probs.argmax()

        disease = le.inverse_transform([y_pred])[0]

        #---------------------------------SHAP-----------------------------------------
        shap_values = explainer.shap_values(input_df, check_additivity=False)

        if isinstance(shap_values, list):
            shap_values_for_pred = shap_values[y_pred][0]
            base_value = explainer.expected_value[y_pred]
        else:
            shap_values_for_pred = shap_values[0, :, y_pred]
            base_value = explainer.expected_value[y_pred]

        # create plot
        plt.figure()

        shap.plots._waterfall.waterfall_legacy(
            base_value,
            shap_values_for_pred,
            feature_names=input_df.columns,
            max_display=10,
            show=False
        )

        # convert plot → base64
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close()
        buf.seek(0)

        shap_img = base64.b64encode(buf.read()).decode("utf-8")

        return {
            "ack":1,
            "prediction": disease,
            "meaning": getMeaning(disease),
            "probabilities": prob_dict,
            "shap_plot": shap_img,
            "confidence": float(probs[y_pred])
        }
    except Exception as e:
        return {"ack":0,"msg":"Some Error Occurred","error":str(e)}
