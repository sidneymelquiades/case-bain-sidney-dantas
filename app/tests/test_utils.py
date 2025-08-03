import os
import joblib
import pytest
from app import utils

class DummyModel:
    def __init__(self, name="modelo"):
        self.name = name

@pytest.fixture
def modelo_dummy():
    return DummyModel()

def test_save_model(modelo_dummy):
    utils.save_model(modelo_dummy)
    assert os.path.exists(utils.MODEL_PATH)
    modelo = joblib.load(utils.MODEL_PATH)
    assert isinstance(modelo, DummyModel)

def test_load_model(modelo_dummy):
    joblib.dump(modelo_dummy, utils.MODEL_PATH)
    modelo_carregado = utils.load_model()
    assert isinstance(modelo_carregado, DummyModel)
    assert modelo_carregado.name == "modelo"

def test_move_model_file(modelo_dummy):
    joblib.dump(modelo_dummy, utils.MODEL_PATH)

    # Move e valida
    utils.move_model_file()
    assert not os.path.exists(utils.MODEL_PATH)
    assert os.path.exists(utils.MODEL_PATH_VERSION)
