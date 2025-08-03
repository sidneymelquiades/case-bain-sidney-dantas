from pipeline.train import train_model

def test_train_model_execucao():
    # Aqui presumimos que train_model() roda sem erro
    try:
        train_model()
    except Exception as e:
        assert False, f"train_model falhou: {e}"