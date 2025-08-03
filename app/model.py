from .schemas import PropertyInput
from .pipeline.utils import load_model
import pandas as pd

model = load_model()

def predict_price(data: PropertyInput):
    df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(df)[0]
    return prediction
