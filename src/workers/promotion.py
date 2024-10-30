import joblib

promotion_model = joblib.load("lib/promotion_model.pkl")

dados = []
features = [dados['feature1'], dados['feature2']]
predicao = promotion_model.predict([features])