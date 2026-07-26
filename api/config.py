from pathlib import Path

from src.biological_age.features.feature_selection import FEATURE_COLUMNS, TARGET_COLUMN

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "final" / "xgb_pipeline_final.pkl"

API_TITLE = "Biological Age Prediction API"
API_DESCRIPTION = "Predict chronological age using NHANES biomarkers."
API_VERSION = "1.0.0"

MODEL_NAME = "XGBoost Biological Age Predictor"
MODEL_VERSION = "1.0.0"

FEATURES = list(FEATURE_COLUMNS)
TARGET = TARGET_COLUMN
