from enum import Enum

from pydantic import BaseModel


class Sex(str, Enum):
    female = "Female"
    male = "Male"


class PredictionRequest(BaseModel):

    # Demographic
    sex: Sex

    # Metabolic
    albumin: float
    blood_urea_nitrogen: float
    creatinine: float
    uric_acid: float
    hba1c_percent: float

    # Lipid
    total_cholesterol: float
    hdl_cholesterol: float
    triglycerides: float

    # CBC
    white_blood_cell_count: float
    lymphocyte_percent: float
    monocyte_percent: float
    neutrophil_percent: float
    red_blood_cell_count: float
    hemoglobin: float
    hematocrit: float
    mean_corpuscular_volume: float
    red_cell_distribution_width: float
    platelet_count: float

    # Electrolytes
    calcium: float
    sodium_si: float
    potassium_si: float
    phosphorus: float

    # Liver
    total_bilirubin: float
    total_protein: float
    globulin: float
    ggt_si: float

    # Engineered
    bun_creatinine_ratio: float
    albumin_globulin_ratio: float
    cholesterol_hdl_ratio: float
    triglyceride_hdl_ratio: float


class PredictionResponse(BaseModel):

    predicted_age: float
    model_name: str
    model_version: str
