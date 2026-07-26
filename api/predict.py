import logging
import pandas as pd

from fastapi import APIRouter, HTTPException

from api.config import MODEL_NAME, MODEL_VERSION
from api.model import pipeline
from api.schemas import PredictionRequest, PredictionResponse, Sex


logger = logging.getLogger(__name__)

router = APIRouter()

SEX_MAPPING = {
    Sex.female: 0,
    Sex.male: 1,
}


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    data = request.model_dump()

    data["sex"] = SEX_MAPPING[request.sex]

    input_df = pd.DataFrame([data])

    logger.info("Post /predict request received")

    try:
        prediction = pipeline.predict(input_df)

        logger.info("Post /predict request processed successfully")

    except Exception as e:

        logger.exception("Prediction failed: %s", str(e))

        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please check the input data and try again."
        )

    return PredictionResponse(
        predicted_age=float(prediction[0]),
        model_name=MODEL_NAME,
        model_version=MODEL_VERSION,
    )
