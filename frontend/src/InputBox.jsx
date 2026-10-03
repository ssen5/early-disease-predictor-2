import React, { useEffect, useState } from "react";

export default function InputBox() {
  const [allSymptoms, setAllSymptoms] = useState([]);
  const [search, setSearch] = useState("");
  const [filtered, setFiltered] = useState([]);
  const [selected, setSelected] = useState([]);
  const [output, setOutput] = useState(null);
  const [loading, setLoading] = useState(false);

  const styles = {
    page: {
      display: "flex",
      height: "100vh",
      background: "linear-gradient(135deg, #0f172a, #1e293b)",
      color: "#e2e8f0",
      fontFamily: "Inter, sans-serif",
    },

    left: {
      width: "30%",
      padding: "30px",
      borderRight: "1px solid rgba(255,255,255,0.1)",
    },

    right: {
      flex: 1,
      padding: "40px",
      overflowY: "auto",
    },

    title: {
      fontSize: "22px",
      fontWeight: "600",
      marginBottom: "20px",
    },

    input: {
      width: "100%",
      padding: "12px",
      borderRadius: "10px",
      border: "none",
      background: "#1e293b",
      color: "#fff",
      marginBottom: "10px",
    },

    list: {
      maxHeight: "150px",
      overflowY: "auto",
      background: "#1e293b",
      borderRadius: "10px",
      marginBottom: "15px",
    },

    listItem: {
      padding: "10px",
      cursor: "pointer",
      borderBottom: "1px solid rgba(255,255,255,0.05)",
    },

    selectedBox: {
      marginTop: "10px",
      maxHeight: "200px",
      overflowY: "auto",
      background: "#1e293b",
      borderRadius: "10px",
      marginBottom: "10px",
    },

    selectedItem: {
      padding: "10px",
      borderBottom: "1px solid rgba(255,255,255,0.05)",
      cursor: "pointer",
      display: "flex",
      justifyContent: "space-between",
    },

    remove: {
      color: "#ef4444",
      fontSize: "12px",
    },

    button: {
      width: "100%",
      padding: "12px",
      borderRadius: "10px",
      border: "none",
      background: "#2563eb",
      color: "#fff",
      cursor: "pointer",
      marginTop: "10px",
    },

    topRow: {
      display: "flex",
      gap: "20px",
      marginBottom: "20px",
    },

    halfCard: {
      flex: 1,
      background: "rgba(255,255,255,0.05)",
      borderRadius: "16px",
      padding: "20px",
    },

    bigPrediction: {
      fontSize: "28px",
      fontWeight: "700",
      color: "#38bdf8",
    },

    subText: {
      color: "#94a3b8",
      marginBottom: "10px",
    },

    sectionTitle: {
      fontSize: "12px",
      textTransform: "uppercase",
      letterSpacing: "1px",
      color: "#38bdf8",
      marginBottom: "8px",
    },

    resultCard: {
      background: "rgba(255,255,255,0.05)",
      borderRadius: "16px",
      padding: "25px",
      marginBottom: "20px",
    },

    listStyle: {
      paddingLeft: "20px",
    },

    probItem: {
      marginBottom: "10px",
    },

    probHeader: {
      display: "flex",
      justifyContent: "space-between",
      fontSize: "13px",
    },

    probBarContainer: {
      width: "100%",
      height: "5px",
      background: "#1e293b",
      borderRadius: "10px",
      marginTop: "4px",
    },

    probBar: {
      height: "100%",
      borderRadius: "10px",
    },

    loader: {
      textAlign: "center",
      marginTop: "50px",
    },

    spinner: {
      width: "40px",
      height: "40px",
      border: "4px solid #334155",
      borderTop: "4px solid #38bdf8",
      borderRadius: "50%",
      margin: "10px auto",
      animation: "spin 1s linear infinite",
    },

    image: {
      width: "100%",
      borderRadius: "10px",
    },

    placeholder: {
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      height: "100%",
      textAlign: "center",
      color: "#64748b",
    },

    placeholderTitle: {
      fontSize: "24px",
      marginBottom: "10px",
      color: "#94a3b8",
    },

    placeholderText: {
      maxWidth: "400px",
      lineHeight: "1.6",
    },
  };

  useEffect(() => {
    fetch("http://127.0.0.1:8000/symptoms")
      .then((res) => res.json())
      .then((data) => setAllSymptoms(data.symptoms));
  }, []);

  useEffect(() => {
    if (!search) setFiltered([]);
    else {
      setFiltered(
        allSymptoms.filter((s) =>
          s.toLowerCase().includes(search.toLowerCase())
        )
      );
    }
  }, [search, allSymptoms]);

  const addSymptom = (s) => {
    if (!selected.includes(s)) setSelected([...selected, s]);
    setSearch("");
  };

  const removeSymptom = (s) => {
    setSelected(selected.filter((x) => x !== s));
  };

  const handleSubmit = async () => {
    setLoading(true);
    setOutput(null);

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input: selected }),
    });

    const data = await res.json();
    setOutput(data);
    setLoading(false);
  };

  const toArray = (val) => (Array.isArray(val) ? val : [val]);

  return (
    <div style={styles.page}>
      {/* LEFT */}
      <div style={styles.left}>
        <div style={styles.title}>Enter Symptoms</div>

        <input
          style={styles.input}
          placeholder="Search symptoms..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <div style={styles.list}>
          {filtered.map((s, i) => (
            <div key={i} style={styles.listItem} onClick={() => addSymptom(s)}>
              {s}
            </div>
          ))}
        </div>

        <div style={styles.selectedBox}>
          {selected.map((s, i) => (
            <div key={i} style={styles.selectedItem} onClick={() => removeSymptom(s)}>
              {s}
              <span style={styles.remove}>✖</span>
            </div>
          ))}
        </div>

        <button style={styles.button} onClick={handleSubmit}>
          Predict
        </button>
      </div>

      {/* RIGHT */}
      <div style={styles.right}>
        {loading && (
          <div style={styles.loader}>
            <div style={styles.spinner}></div>
            Analyzing...
          </div>
        )}

        {!loading && !output && (
          <div style={styles.placeholder}>
            <h2 style={styles.placeholderTitle}>No Results Yet</h2>
            <p style={styles.placeholderText}>
              Your result and its details will be displayed here once you select
              symptoms and click predict.
            </p>
          </div>
        )}

        {output && output.ack === 1 && (
          <>
            <div style={styles.topRow}>
              <div style={styles.halfCard}>
                <div style={styles.subText}>Probably</div>
                <div style={styles.bigPrediction}>{output.prediction}</div>
                <div style={styles.subText}>
                  Confidence: {(output.confidence * 100).toFixed(2)}%
                </div>
              </div>

              <div style={styles.halfCard}>
                <div style={styles.sectionTitle}>Other Possibilities</div>
                {Object.entries(output.probabilities)
                  .sort((a, b) => b[1] - a[1])
                  .map(([d, p], i) => (
                    <div key={i} style={styles.probItem}>
                      <div style={styles.probHeader}>
                        <span>{d}</span>
                        <span>{(p * 100).toFixed(1)}%</span>
                      </div>
                      <div style={styles.probBarContainer}>
                        <div
                          style={{
                            ...styles.probBar,
                            width: `${p * 100}%`,
                            background: i === 0 ? "#38bdf8" : "#64748b",
                          }}
                        />
                      </div>
                    </div>
                  ))}
              </div>
            </div>

            <div style={styles.resultCard}>
              <div style={styles.sectionTitle}>Description</div>
              <p>{output.meaning.description}</p>

              <div style={styles.sectionTitle}>Tests</div>
              <ul style={styles.listStyle}>
                {toArray(output.meaning.tests).map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>

              <div style={styles.sectionTitle}>Care</div>
              <ul style={styles.listStyle}>
                {toArray(output.meaning.care).map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>

            <div style={styles.resultCard}>
              <h4>Why this prediction?</h4>
              <img
                src={`data:image/png;base64,${output.shap_plot}`}
                alt="SHAP"
                style={styles.image}
              />
            </div>
          </>
        )}
      </div>

      <style>
        {`
        @keyframes spin {
          100% { transform: rotate(360deg); }
        }
        `}
      </style>
    </div>
  );
}