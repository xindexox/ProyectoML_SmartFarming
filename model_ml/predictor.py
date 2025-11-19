from joblib import load
import os
import pandas as pd

_model = None


def load_model():
    global _model
    if _model is None:
        model_path = os.path.join(os.path.dirname(__file__), "modelo_smart_farming.joblib")
        _model = load(model_path)
    return _model


def predict_from_dict(data: dict):
    """
    Recibe un diccionario con TODAS las features:
    ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'soil_moisture',
     'soil_type', 'sunlight_exposure', 'wind_speed', 'co2_concentration',
     'organic_matter', 'irrigation_frequency', 'crop_density', 'pest_pressure',
     'fertilizer_usage', 'growth_stage', 'urban_area_proximity',
     'water_source_type', 'frost_risk', 'water_usage_efficiency']
    """
    df = pd.DataFrame([data])
    model = load_model()
    y_pred = model.predict(df)
    return y_pred[0]
