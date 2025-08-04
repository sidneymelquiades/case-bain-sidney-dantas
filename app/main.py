from fastapi import FastAPI, HTTPException, Header
from .model import predict_price
from .schemas import PropertyInput, PredictionOutput
from .logger import get_logger
from .pipeline.configloader import load_config
from pathlib import Path

config = load_config()
description = Path(__file__).resolve().parents[1].joinpath("README.md").read_text(encoding="utf-8")
app = FastAPI(title="Case Bain and Company",
    description=description,
    version="1.0.0",
    contact={
        "name": "Sidney Dantas",
        "email": "sidneymelquiadesdantas@gmail.com",
        "url": "https://github.com/sidneymelquiades"
    })

logger = get_logger()
DATA_PATH = config['paths']['data_main'] # Pasta onde estão os arquivos train.csv e test.csv

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PropertyInput, api_key: str = Header(...)):
    verify_api_key(api_key)

    try:
        prediction = predict_price(data)
        logger.info(f"Prediction: {prediction} | Input: {data.dict()}")
        return {"price": prediction}
    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")


