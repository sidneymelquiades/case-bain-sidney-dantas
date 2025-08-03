from fastapi import FastAPI, Depends, HTTPException, Header, UploadFile, File
from app.model import predict_price
from app.schemas import PropertyInput, PredictionOutput
from app.auth import verify_api_key
from app.logger import get_logger
from pipeline.train import train_model
from pipeline.configloader import load_config
import os
import shutil
from pathlib import Path

config = load_config()
description = Path("README.md").read_text(encoding="utf-8")
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

@app.post("/retrain")
def retrain_model(
    train_file: UploadFile = File(...),
    test_file: UploadFile = File(...),
    api_key: str = Header(...)
):
    verify_api_key(api_key)

    try:
        train_path = os.path.join(DATA_PATH, "train.csv")
        test_path = os.path.join(DATA_PATH, "test.csv")

        # Salva os arquivos recebidos
        with open(train_path, "wb") as f:
            shutil.copyfileobj(train_file.file, f)

        with open(test_path, "wb") as f:
            shutil.copyfileobj(test_file.file, f)

        # Executa o retrain
        train_model()

        logger.info("Modelo re-treinado com sucesso.")
        return {"detail": "Modelo re-treinado com sucesso."}

    except Exception as e:
        logger.error(f"Erro ao re-treinar modelo: {e}")
        raise HTTPException(status_code=500, detail="Erro ao re-treinar modelo.")