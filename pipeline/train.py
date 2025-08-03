
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
from category_encoders import TargetEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from pipeline.utils import save_model, move_model_file
from pipeline.configloader import load_config

    
config = load_config()


### função a ser refatorada caso mudemos para um banco de dados
### ou outra fonte
def load_data():
    test_path=config['paths']['test_data']
    train_path=config['paths']['train_data']
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test

def print_metrics(predictions, target):
    print("RMSE:", np.sqrt(mean_squared_error(predictions, target)))
    print("MAPE:", mean_absolute_percentage_error(predictions, target))
    print("MAE :", mean_absolute_error(predictions, target))

def train_model():
    train, test = load_data()

    # Feature selection
    features = [col for col in train.columns if col not in ['id', 'target', 'price']]
    categorical_cols = ["type", "sector"]
    target = "price"

    # Pipeline
    categorical_transformer = TargetEncoder()

    preprocessor = ColumnTransformer(
        transformers=[
            ('categorical', categorical_transformer, categorical_cols)
        ],
        remainder='passthrough'
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', GradientBoostingRegressor(
            learning_rate=0.01,
            n_estimators=300,
            max_depth=5,
            loss="absolute_error"
        ))
    ])

    pipeline.fit(train[features], train[target])

    predictions = pipeline.predict(test[features])
    print_metrics(predictions, test[target].values)
    try:
        move_model_file()
    except:
        pass
    
    save_model(pipeline)

if __name__ == "__main__":
    train_model()