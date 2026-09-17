from fastapi import FastAPI
from agent.anomaly_detector import detect_anomalies

app = FastAPI(title="AIOps Community API")

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/analyze")
def analyze_metrics(payload: dict):
    results = detect_anomalies(payload.get("data", []))
    return {"anomalies": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
