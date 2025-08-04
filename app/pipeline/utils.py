import joblib
import os
import shutil
from datetime import datetime
from .configloader import load_config

    
config = load_config()


MODEL_PATH = config['paths']['model_output']
MODEL_PATH_VERSION = config['paths']['versions']+datetime.now().strftime("%Y-%m-%d-%H_%M_%S")+'.joblib'

def save_model(model):
    os.makedirs("app", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

def load_model():
    return joblib.load(MODEL_PATH)


