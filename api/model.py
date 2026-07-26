from joblib import load

from api.config import MODEL_PATH

pipeline = load(MODEL_PATH)
MODEL_LOADED = pipeline is not None
