from fastapi import FastAPI


from api.config import API_DESCRIPTION, API_TITLE, API_VERSION
from api.routes import router as base_router
from api.predict import router as predict_router


app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
)

app.include_router(base_router)
app.include_router(predict_router)
