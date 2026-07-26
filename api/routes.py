from fastapi import APIRouter

from api.config import API_VERSION, FEATURE_COLUMNS, MODEL_NAME, MODEL_VERSION
from api.model import MODEL_LOADED

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Biological Age Prediction API",
        "version": API_VERSION,
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": MODEL_LOADED,
    }


@router.get("/model-info")
def model_info():
    return {
        "model_name": MODEL_NAME,
        "model_version": MODEL_VERSION,
        "target": "age_years",
        "n_features": len(FEATURE_COLUMNS),
        "features": FEATURE_COLUMNS,
    }
