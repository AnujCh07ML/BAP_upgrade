# 🧬 Biological Age Prediction using NHANES Biomarkers

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-success?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Deployment](https://img.shields.io/badge/Deployment-Render-46E3B7)

> **An end-to-end machine learning project for predicting chronological age from routine clinical laboratory biomarkers using the National Health and Nutrition Examination Survey (NHANES).**

This project demonstrates a **production-oriented machine learning workflow** that extends beyond model training to include software engineering, model explainability, automated testing, containerization, CI/CD, and cloud deployment.

The project was developed to simulate how machine learning systems are built, tested, packaged, and deployed in production environments.

---

# 🚀 Live Demo

### 🌐 API Base URL

https://biological-age-prediction-zhbi.onrender.com

### 📄 Interactive API Documentation (Swagger)

https://biological-age-prediction-zhbi.onrender.com/docs

---

# ⭐ Project Highlights

- **36,992** NHANES participants (2011–2020)
- **27 original predictor features**
- **30 predictor features after biologically inspired feature engineering**
- **Best Model:** Feature Engineered XGBoost
- **MAE:** **7.56 years**
- **RMSE:** **10.67 years**
- **R²:** **0.801**
- SHAP-based global and local model explainability
- Production-ready FastAPI inference service
- Dockerized deployment
- Automated testing with Pytest
- Continuous Integration using GitHub Actions
- Public cloud deployment on Render

---

# 📖 Project Overview

Chronological age is associated with measurable physiological changes across multiple biological systems.

This project investigates whether routinely collected blood biomarkers can accurately predict chronological age using data from the National Health and Nutrition Examination Survey (NHANES).

Rather than focusing solely on model performance, the project emphasizes building a **complete machine learning system** that follows modern software engineering practices.

The repository includes reusable modules for:

- Data ingestion
- Data harmonization
- Dataset creation
- Feature engineering
- Data preprocessing
- Model training
- Hyperparameter optimization
- Model evaluation
- Explainable AI (SHAP)
- REST API deployment
- Automated testing
- Docker containerization
- Continuous Integration

The result is a modular, reproducible, and deployable machine learning project suitable for production-style workflows.

---

# 📊 Dataset

## Source

**National Health and Nutrition Examination Survey (NHANES)**

Conducted by the Centers for Disease Control and Prevention (CDC).

---

## Study Period

**2011–2020**

---

## Dataset Summary

| Metric                        |             Value |
| ----------------------------- | ----------------: |
| Participants                  |            36,992 |
| Original Predictor Features   |                27 |
| Engineered Predictor Features |                30 |
| Target Variable               | Chronological Age |

---

# ⚙️ Machine Learning Pipeline

```text
Raw NHANES Data
        │
        ▼
Load & Merge Data
        │
        ▼
Dataset Creation
        │
        ▼
Feature Engineering
        │
        ▼
Feature Selection
        │
        ▼
Train/Test Split
        │
        ▼
Preprocessing Pipeline
        │
        ▼
Hyperparameter Optimization
        │
        ▼
Model Evaluation
        │
        ▼
SHAP Explainability
        │
        ▼
FastAPI REST API
        │
        ▼
Docker
        │
        ▼
GitHub Actions CI
        │
        ▼
Cloud Deployment (Render)
```

---

# 🧬 Feature Engineering

Three biologically meaningful biomarkers were engineered using established clinical relationships.

| Engineered Feature       | Formula                 |
| ------------------------ | ----------------------- |
| Albumin / Globulin Ratio | Albumin ÷ Globulin      |
| Cholesterol / HDL Ratio  | Total Cholesterol ÷ HDL |
| Triglyceride / HDL Ratio | Triglycerides ÷ HDL     |

These engineered biomarkers consistently improved predictive performance over the tuned baseline model while remaining clinically interpretable.

---

# 🤖 Models Evaluated

Three tree-based regression algorithms were evaluated.

- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Hyperparameter optimization was performed using **RandomizedSearchCV** with cross-validation to identify the best-performing configuration for each model.

---

# 🏆 Model Performance

| Model                              |      MAE |      RMSE |        R² |
| ---------------------------------- | -------: | --------: | --------: |
| Random Forest                      |     8.05 |     11.30 |     0.777 |
| Tuned XGBoost (V1)                 |     7.71 |     10.75 |     0.798 |
| Tuned LightGBM                     |     7.71 |     10.73 |     0.799 |
| ⭐ Feature Engineered XGBoost (V2) | **7.56** | **10.67** | **0.801** |

---

# 📈 Feature Engineering Impact

| Metric | Tuned Baseline | Feature Engineered |
| ------ | -------------: | -----------------: |
| MAE    |           7.71 |           **7.56** |
| RMSE   |          10.75 |          **10.67** |
| R²     |          0.798 |          **0.801** |

The addition of biologically inspired ratio features produced measurable improvements across every evaluation metric while maintaining model interpretability.

---

# 🏅 Final Production Model

The **Feature Engineered XGBoost (V2)** pipeline was selected as the production model based on:

- Lowest Mean Absolute Error (MAE)
- Lowest Root Mean Squared Error (RMSE)
- Highest coefficient of determination (R²)
- Consistent SHAP explanations
- End-to-end preprocessing pipeline
- Serialized production-ready inference pipeline

Production artifact:

```text
models/final/xgb_pipeline_final.pkl
```

---

# 🔍 Model Explainability (SHAP)

Model predictions were interpreted using **SHAP (SHapley Additive exPlanations)** to understand both global feature importance and individual prediction behavior.

This analysis was used not only to explain the model but also to guide the feature engineering process.

---

## Global Feature Importance

![SHAP Feature Importance](outputs/plots/shap_bar_v2.png)

The SHAP feature importance plot ranks predictors according to their average contribution across all predictions.

---

## SHAP Beeswarm Plot

![SHAP Beeswarm](outputs/plots/shap_beeswarm_v2.png)

The beeswarm visualization illustrates both the magnitude and direction of each feature's influence while highlighting interactions and variability across participants.

---

## Feature Dependence

### HbA1c

![HbA1c Dependence](outputs/plots/numeric__hba1c_percent_dependence_v2.png)

Higher HbA1c values were consistently associated with increased predicted age, making glycemic regulation one of the strongest aging-related biomarkers in the model.

---

### Mean Corpuscular Volume (MCV)

![MCV Dependence](outputs/plots/numeric__mean_corpuscular_volume_dependence_v2.png)

Mean Corpuscular Volume demonstrated a nonlinear relationship with predicted age, indicating age-dependent changes in red blood cell characteristics.

---

# 🧠 Key Findings

The SHAP analysis revealed several biologically meaningful observations:

- HbA1c was the strongest predictor of chronological age.
- Mean Corpuscular Volume exhibited a nonlinear relationship with aging.
- Blood Urea Nitrogen and Total Cholesterol consistently contributed to age prediction.
- Phosphorus demonstrated an inverse relationship with predicted age.
- The engineered ratio features improved model performance while complementing, rather than replacing, the original laboratory biomarkers.

---

# 🌐 REST API

The production model is served through a **FastAPI** application, enabling real-time predictions via a REST API.

### Available Endpoints

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | `/`           | API information           |
| GET    | `/health`     | Service health check      |
| GET    | `/model-info` | Model metadata            |
| POST   | `/predict`    | Predict chronological age |

Interactive API documentation is available at:

### Swagger UI

https://biological-age-prediction-zhbi.onrender.com/docs

---

# 📤 Example Prediction Request

```json
{
  "sex": "Male",
  "albumin": 4.4,
  "blood_urea_nitrogen": 15.0,
  "creatinine": 0.92,
  "uric_acid": 5.4,
  "hba1c_percent": 5.3,
  "total_cholesterol": 184,
  "hdl_cholesterol": 52,
  "triglycerides": 108,
  "white_blood_cell_count": 6.7,
  "lymphocyte_percent": 33,
  "monocyte_percent": 8,
  "neutrophil_percent": 56,
  "red_blood_cell_count": 4.8,
  "hemoglobin": 14.8,
  "hematocrit": 44.3,
  "mean_corpuscular_volume": 92,
  "red_cell_distribution_width": 13.1,
  "platelet_count": 258,
  "calcium": 9.4,
  "sodium_si": 140,
  "potassium_si": 4.2,
  "phosphorus": 3.8,
  "total_bilirubin": 0.7,
  "total_protein": 7.1,
  "globulin": 2.8,
  "ggt_si": 18
}
```

---

# 📥 Example Response

```json
{
  "predicted_age": 42.63,
  "model_name": "XGBoost Biological Age Predictor",
  "model_version": "1.0.0"
}
```

---

# 🐳 Docker

The application can be executed locally using Docker.

## Build the image

```bash
docker build -t biological-age-api .
```

## Run the container

```bash
docker run -p 8000:8000 biological-age-api
```

The API will be available at:

```
http://localhost:8000/docs
```

---

# ☁️ Cloud Deployment

The application is publicly deployed on **Render** using Docker.

Deployment workflow:

```text
GitHub
    │
    ▼
GitHub Actions
    │
    ▼
Docker Image
    │
    ▼
Render
    │
    ▼
Public FastAPI Service
```

Live deployment:

https://biological-age-prediction-zhbi.onrender.com

---

# ✅ Running Tests

Run the complete test suite from the project root:

```bash
python -m pytest
```

Run a specific test module:

```bash
python -m pytest tests/test_api.py -v
```

---

## Why use `python -m pytest`?

This project contains multiple top-level packages (`api/` and `src/`).

Executing tests with

```bash
python -m pytest
```

ensures Python uses the active interpreter and correctly resolves the project's module search path, avoiding import errors such as:

```text
ModuleNotFoundError: No module named 'api'
```

Using `python -m pytest` is the recommended way to execute the project's test suite.

---

# 📁 Repository Structure

```text
biological-age-prediction/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── api/
│   ├── app.py
│   ├── config.py
│   ├── model.py
│   ├── routes.py
│   ├── predict.py
│   └── schemas.py
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│   ├── tuned/
│   ├── feature_engineered/
│   └── final/
│       └── xgb_pipeline_final.pkl
│
├── notebooks/
│
├── outputs/
│   ├── metrics/
│   ├── plots/
│   ├── reports/
│   └── tuning/
│
├── src/
│   └── biological_age/
│       ├── data/
│       ├── evaluation/
│       ├── features/
│       ├── interpret/
│       ├── models/
│       ├── preprocessing/
│       ├── split/
│       └── utils/
│
├── tests/
│
├── Dockerfile
├── .dockerignore
├── config.yaml
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🛠️ Technology Stack

## Data Processing

- Pandas
- NumPy

---

## Machine Learning

- Scikit-learn
- XGBoost
- LightGBM

---

## Explainability

- SHAP

---

## Backend

- FastAPI
- Pydantic
- Uvicorn

---

## Software Engineering

- Pytest
- Docker
- GitHub Actions
- Render
- Git

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/AnujCh07ML/biological-age-prediction.git

cd biological-age-prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt

pip install -e .
```

Run the complete training pipeline:

```bash
python main.py
```

Start the FastAPI server locally:

```bash
uvicorn api.app:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

# 📌 Project Status

## ✅ Completed

- Multi-cycle NHANES data ingestion
- Data harmonization and preprocessing
- Feature engineering
- Hyperparameter optimization
- Model evaluation
- SHAP explainability
- Production model selection
- FastAPI inference service
- Automated testing with Pytest
- Docker containerization
- GitHub Actions CI pipeline
- Cloud deployment on Render

---

## 🚀 Future Improvements

- MLflow experiment tracking
- Model monitoring
- Automated model retraining
- External validation dataset
- Biological age proxy estimation

---

# 💡 Lessons Learned

Building the predictive model was only one part of the project.

The larger challenge involved developing a complete machine learning system that is reproducible, explainable, testable, containerized, and deployable.

Through this project, I gained practical experience with:

- Designing modular ML pipelines
- Building reusable preprocessing workflows
- Applying explainable AI using SHAP
- Creating production-ready REST APIs
- Writing automated tests
- Containerizing applications with Docker
- Implementing continuous integration
- Deploying machine learning models to the cloud

---

# 👤 Author

**Anuj Chauhan**

Machine Learning • Bioinformatics • Explainable AI

I am passionate about applying machine learning to computational biology, aging research, and biomedical data science, with a long-term goal of developing AI systems that contribute to healthier human aging.

- GitHub: https://github.com/AnujCh07ML
- LinkedIn: https://www.linkedin.com/in/anujch07ml/

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.
