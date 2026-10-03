import React, { useEffect, useState } from "react";
import InputBox from "./InputBox";

export default function App() {
  const [page, setPage] = useState("home");

  // 🔥 Fix white background
  useEffect(() => {
    document.body.style.margin = "0";
    document.body.style.padding = "0";
    document.body.style.background = "#0f172a";
  }, []);

  const styles = {
    container: {
      minHeight: "100vh",
      width: "100%",
      background: "linear-gradient(135deg, #0f172a, #1e293b)",
      color: "#e2e8f0",
      fontFamily: "Inter, sans-serif",
    },

    navbar: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "15px 30px",
      borderBottom: "1px solid rgba(255,255,255,0.1)",
      background: "rgba(15,23,42,0.9)",
      backdropFilter: "blur(10px)",
    },

    logo: {
      fontSize: "18px",
      fontWeight: "600",
      color: "#38bdf8",
    },

    navBtns: {
      display: "flex",
      gap: "10px",
    },

    btn: (active) => ({
      padding: "8px 16px",
      borderRadius: "8px",
      border: "none",
      cursor: "pointer",
      background: active ? "#38bdf8" : "transparent",
      color: active ? "#0f172a" : "#e2e8f0",
      border: "1px solid rgba(255,255,255,0.1)",
      transition: "0.2s",
    }),

    content: {
      height: "calc(100vh - 60px)",
      overflow: "auto",
    },

    about: {
      padding: "60px",
      maxWidth: "900px",
      margin: "auto",
      lineHeight: "1.7",
    },

    heading: {
      fontSize: "28px",
      marginBottom: "20px",
      color: "#38bdf8",
    },

    subHeading: {
      marginTop: "25px",
      marginBottom: "10px",
      color: "#94a3b8",
      fontSize: "14px",
      textTransform: "uppercase",
      letterSpacing: "1px",
    },

    text: {
      color: "#cbd5f5",
    },
  };

  return (
    <div style={styles.container}>
      {/* 🔝 NAVBAR */}
      <div style={styles.navbar}>
        <div style={styles.logo}>Early Disease Predictor</div>

        <div style={styles.navBtns}>
          <button
            style={styles.btn(page === "home")}
            onClick={() => setPage("home")}
          >
            Home
          </button>

          <button
            style={styles.btn(page === "about")}
            onClick={() => setPage("about")}
          >
            About
          </button>
        </div>
      </div>

      {/* 📦 CONTENT */}
      <div style={styles.content}>
        {page === "home" && <InputBox />}

        {page === "about" && (
  <div style={styles.about}>
    {/* HEADING */}
    <div style={styles.heading}>About This Project</div>

    {/* INTRO */}
    <p
      style={{
        ...styles.text,
        fontSize: "16px",
        lineHeight: "1.9",
      }}
    >
      Early Disease Predictor is an AI-powered healthcare prediction
      platform developed to assist users in identifying possible diseases
      based on symptoms provided by the user. The system combines machine
      learning with explainable AI techniques to deliver intelligent,
      fast, and transparent disease predictions through an interactive
      web-based interface.
    </p>

    {/* OVERVIEW */}
    <div style={styles.subHeading}>Project Overview</div>

    <div
      style={{
        background: "rgba(255,255,255,0.04)",
        border: "1px solid rgba(255,255,255,0.07)",
        borderRadius: "18px",
        padding: "24px",
        marginTop: "12px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.2)",
      }}
    >
      <p style={styles.text}>
        The prediction model has been trained using a structured medical
        dataset containing multiple diseases and symptom combinations.
        Each symptom is converted into machine-readable features, allowing
        the Random Forest model to recognize hidden relationships between
        symptoms and diseases.
      </p>

      <p style={styles.text}>
        The system is capable of generating probable disease predictions
        along with confidence scores and detailed explainability analysis
        using SHAP (SHapley Additive exPlanations).
      </p>
    </div>

    {/* FEATURES */}
    <div style={styles.subHeading}>Core Features</div>

    <div
      style={{
        marginTop: "16px",
        display: "grid",
        gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
        gap: "16px",
      }}
    >
      {[
        "Symptom-based disease prediction",
        "Top probable diseases with confidence scores",
        "SHAP-powered explainable AI analysis",
        "Interactive and modern user interface",
        "FastAPI backend integration",
        "Machine learning driven predictions",
      ].map((feature, index) => (
        <div
          key={index}
          style={{
            background: "rgba(255,255,255,0.05)",
            border: "1px solid rgba(255,255,255,0.08)",
            borderRadius: "14px",
            padding: "18px",
            display: "flex",
            alignItems: "center",
            gap: "12px",
          }}
        >
          <div
            style={{
              width: "10px",
              height: "10px",
              borderRadius: "50%",
              background: "#38bdf8",
              flexShrink: 0,
            }}
          />

          <div
            style={{
              color: "#e2e8f0",
              fontSize: "15px",
            }}
          >
            {feature}
          </div>
        </div>
      ))}
    </div>

    {/* TECH STACK */}
    <div style={styles.subHeading}>Technology Stack</div>

    <div
      style={{
        marginTop: "16px",
        display: "grid",
        gridTemplateColumns: "repeat(4, minmax(0, 1fr))",
        gap: "16px",
      }}
    >
      {[
        ["React", "Frontend"],
        ["FastAPI", "Backend"],
        ["Random Forest", "ML Model"],
        ["SHAP", "xAI"],
      ].map(([title, subtitle]) => (
        <div
          key={title}
          style={{
            background:
              "linear-gradient(135deg, rgba(56,189,248,0.08), rgba(255,255,255,0.03))",
            border: "1px solid rgba(56,189,248,0.12)",
            borderRadius: "16px",
            padding: "20px",
            textAlign: "center",
          }}
        >
          <div
            style={{
              fontSize: "18px",
              fontWeight: "700",
              color: "#f8fafc",
              marginBottom: "6px",
            }}
          >
            {title}
          </div>

          <div
            style={{
              color: "#94a3b8",
              fontSize: "14px",
            }}
          >
            {subtitle}
          </div>
        </div>
      ))}
    </div>

    {/* TEAM SECTION */}
    <div style={styles.subHeading}>Project Team</div>

    <div
      style={{
        marginTop: "18px",
        display: "grid",
        gridTemplateColumns: "repeat(4, minmax(0, 1fr))",
        gap: "16px",
      }}
    >
      {[
        ["ARITRA BHANDARI", "BWU/BTA/22/246"],
        ["PRIYAJIT DUTTA", "BWU/BTA/22/275"],
        ["SOUMYOJIT SEN", "BWU/BTA/22/286"],
        ["GAGAN BISWAS", "BWU/BTA/22/294"],
      ].map(([name, id]) => (
        <div
          key={id}
          style={{
            background: "rgba(255,255,255,0.05)",
            border: "1px solid rgba(255,255,255,0.08)",
            borderRadius: "18px",
            padding: "20px",
            textAlign: "center",
            boxShadow: "0 8px 20px rgba(0,0,0,0.25)",
          }}
        >
          <div
            style={{
              width: "58px",
              height: "58px",
              borderRadius: "50%",
              background: "linear-gradient(135deg, #38bdf8, #0ea5e9)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontWeight: "700",
              fontSize: "20px",
              color: "#0f172a",
              margin: "0 auto 14px auto",
            }}
          >
            {name.charAt(0)}
          </div>

          <div
            style={{
              fontSize: "15px",
              fontWeight: "700",
              color: "#f8fafc",
              marginBottom: "8px",
              lineHeight: "1.4",
            }}
          >
            {name}
          </div>

          <div
            style={{
              fontSize: "13px",
              color: "#94a3b8",
              letterSpacing: "0.4px",
            }}
          >
            {id}
          </div>
        </div>
      ))}
    </div>

    {/* MENTOR */}
    <div style={styles.subHeading}>Project Mentor</div>

    <div
      style={{
        marginTop: "18px",
        background:
          "linear-gradient(135deg, rgba(56,189,248,0.12), rgba(14,165,233,0.05))",
        border: "1px solid rgba(56,189,248,0.2)",
        borderRadius: "20px",
        padding: "24px",
        display: "flex",
        alignItems: "center",
        gap: "18px",
        boxShadow: "0 8px 25px rgba(0,0,0,0.25)",
      }}
    >
      <div
        style={{
          width: "70px",
          height: "70px",
          borderRadius: "50%",
          background: "linear-gradient(135deg, #38bdf8, #0284c7)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: "26px",
          fontWeight: "700",
          color: "#0f172a",
          flexShrink: 0,
        }}
      >
        P
      </div>

      <div>
        <div
          style={{
            fontSize: "22px",
            fontWeight: "700",
            color: "#f8fafc",
            marginBottom: "6px",
          }}
        >
          Mrs Pranashi Chakraborty
        </div>

        <div
          style={{
            color: "#94a3b8",
            fontSize: "15px",
          }}
        >
          Mentor • BTech CSE-AI
        </div>
      </div>
    </div>
  </div>
)}
      </div>
    </div>
  );
}