from fastapi.testclient import TestClient

from api.app import app

from api.config import (
    MODEL_NAME,
    MODEL_VERSION,
    FEATURE_COLUMNS,
)


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()[
        "message"] == ("Biological Age Prediction API")


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True


def test_model_info():
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model_name"] == MODEL_NAME
    assert data["model_version"] == MODEL_VERSION
    assert data["target"] == "age_years"
    assert data["n_features"] == len(FEATURE_COLUMNS)
    assert data["features"] == FEATURE_COLUMNS


def test_predict():

    request = {
        "sex": "Male",
        "albumin": 4.3,
        "blood_urea_nitrogen": 14.0,
        "creatinine": 0.9,
        "uric_acid": 5.4,
        "hba1c_percent": 5.3,
        "total_cholesterol": 180.0,
        "hdl_cholesterol": 50.0,
        "triglycerides": 120.0,
        "white_blood_cell_count": 6.5,
        "lymphocyte_percent": 32.0,
        "monocyte_percent": 7.0,
        "neutrophil_percent": 58.0,
        "red_blood_cell_count": 5.0,
        "hemoglobin": 15.0,
        "hematocrit": 45.0,
        "mean_corpuscular_volume": 90.0,
        "red_cell_distribution_width": 13.0,
        "platelet_count": 250.0,
        "calcium": 9.4,
        "sodium_si": 140.0,
        "potassium_si": 4.2,
        "phosphorus": 3.8,
        "total_bilirubin": 0.8,
        "total_protein": 7.2,
        "globulin": 2.8,
        "ggt_si": 20.0,
        "bun_creatinine_ratio": 15.6,
        "albumin_globulin_ratio": 1.54,
        "cholesterol_hdl_ratio": 3.6,
        "triglyceride_hdl_ratio": 2.4,
    }

    response = client.post(
        "/predict",
        json=request,
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_age" in data
    assert isinstance(data["predicted_age"], float)
    assert data["predicted_age"] > 0

    assert data["model_name"] == MODEL_NAME
    assert data["model_version"] == MODEL_VERSION


def test_invalid_predict_request():

    request = {
        "sex": "Alien",
        "albumin": 4.3,
        "blood_urea_nitrogen": 14.0,
        "creatinine": 0.9,
        "uric_acid": 5.4,
        "hba1c_percent": 5.3,
        "total_cholesterol": 180.0,
        "hdl_cholesterol": 50.0,
        "triglycerides": 120.0,
        "white_blood_cell_count": 6.5,
        "lymphocyte_percent": 32.0,
        "monocyte_percent": 7.0,
        "neutrophil_percent": 58.0,
        "red_blood_cell_count": 5.0,
        "hemoglobin": 15.0,
        "hematocrit": 45.0,
        "mean_corpuscular_volume": 90.0,
        "red_cell_distribution_width": 13.0,
        "platelet_count": 250.0,
        "calcium": 9.4,
        "sodium_si": 140.0,
        "potassium_si": 4.2,
        "phosphorus": 3.8,
        "total_bilirubin": 0.8,
        "total_protein": 7.2,
        "globulin": 2.8,
        "ggt_si": 20.0,
        "bun_creatinine_ratio": 15.6,
        "albumin_globulin_ratio": 1.54,
        "cholesterol_hdl_ratio": 3.6,
        "triglyceride_hdl_ratio": 2.4,
    }

    response = client.post(
        "/predict",
        json=request,
    )

    assert response.status_code == 422
