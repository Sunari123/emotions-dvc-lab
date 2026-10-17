from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI(title="Emotions‑MLOps Demo Service")
MODEL_PATH = Path("ml/registry/model.joblib")
model = joblib.load(MODEL_PATH)

class PredictRequest(BaseModel):
    id_val: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    pred = model.predict([[req.id_val]])[0]
    return {"prediction": float(pred)}