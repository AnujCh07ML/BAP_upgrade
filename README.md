# 🧬 Biological Age Prediction using NHANES Biomarkers

> **An end-to-end machine learning project for predicting chronological age from clinical laboratory biomarkers using the National Health and Nutrition Examination Survey (NHANES).**

This project demonstrates a production-style machine learning workflow, covering:

- Data engineering and preprocessing
- Biologically inspired feature engineering
- Hyperparameter optimization
- Explainable AI (SHAP)
- Modular project architecture
- Model versioning
- Automated testing (Pytest)
- CI/CD with GitHub Actions
- Dockerized environment

---

# ⭐ Project Highlights

- **36,992** NHANES participants (2011–2020)
- **27 original predictor features**
- **30 predictor features after feature engineering**
- **Best Model:** Feature Engineered XGBoost
- **MAE:** **7.56 years**
- **RMSE:** **10.67 years**
- **R²:** **0.801**
- SHAP-based global and local model interpretation
- Production-style modular ML architecture

---

# 📖 Project Overview

Aging is associated with measurable physiological changes across multiple biological systems.

This project investigates whether routinely collected blood biomarkers can accurately predict chronological age and provide a foundation for future biological age estimation.

Unlike notebook-only implementations, this project is structured as a reusable machine learning system with dedicated modules for:

- Data ingestion
- Data preprocessing
- Feature engineering
- Model training
- Hyperparameter tuning
- Model evaluation
- Model interpretation
- Artifact management

---

# 📊 Dataset

### Source

National Health and Nutrition Examination Survey (NHANES)

### Study Period

2011–2020

### Dataset Summary

| Metric                        |             Value |
| ----------------------------- | ----------------: |
| Participants                  |            36,992 |
| Original Predictor Features   |                27 |
| Engineered Predictor Features |                30 |
| Target                        | Chronological Age |

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
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
SHAP Explainability
        │
        ▼
Versioned Model Artifacts
```

---

# 🧬 Feature Engineering

Three biologically motivated biomarkers were engineered using established clinical knowledge.

| Engineered Feature       | Formula                 |
| ------------------------ | ----------------------- |
| Albumin / Globulin Ratio | Albumin ÷ Globulin      |
| Cholesterol / HDL Ratio  | Total Cholesterol ÷ HDL |
| Triglyceride / HDL Ratio | Triglycerides ÷ HDL     |

These engineered biomarkers improved predictive performance over the tuned baseline model.

---

# 🤖 Models Evaluated

- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Hyperparameter optimization was performed using **RandomizedSearchCV** with cross-validation.

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

The addition of biologically meaningful ratio features produced consistent improvements across all evaluation metrics.

---

# 🏅 Final Production Model

The **Feature Engineered XGBoost (V2)** model was selected as the production model based on:

- Lowest MAE
- Lowest RMSE
- Highest R²
- Consistent SHAP interpretation
- Modular preprocessing pipeline
- Versioned model artifacts

Production artifact:

```text
models/final/xgb_pipeline_final.pkl
```

---

# 🔍 Model Explainability (SHAP)

Global and local explanations were generated using SHAP.

## Global Feature Importance

![SHAP Feature Importance](outputs/plots/shap_bar_v2.png)

---

## SHAP Beeswarm

![SHAP Beeswarm](outputs/plots/shap_beeswarm_v2.png)

---

## Feature Dependence

### HbA1c

![HbA1c Dependence](outputs/plots/numeric__hba1c_percent_dependence_v2.png)

### Mean Corpuscular Volume

![MCV Dependence](outputs/plots/numeric__mean_corpuscular_volume_dependence_v2.png)

---

# 🧠 Key Findings

SHAP analysis identified several biologically meaningful patterns:

- HbA1c was the strongest predictor of chronological age.
- Mean Corpuscular Volume demonstrated a pronounced nonlinear relationship with aging.
- Blood Urea Nitrogen and Total Cholesterol were consistently influential biomarkers.
- Phosphorus exhibited an inverse relationship with predicted age.
- The engineered ratio features improved predictive performance while complementing the original biomarkers rather than replacing them.

---

# 📁 Repository Structure

```text
biological-age-prediction/

├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│   ├── tuned/
│   ├── feature_engineered/
│   └── final/
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
│       ├── api/
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
├── .github/
├── Dockerfile
├── config.yaml
├── main.py
└── README.md
```

---

# 🛠️ Technology Stack

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- XGBoost
- LightGBM

### Explainability

- SHAP

### Software Engineering

- Pytest
- Git
- GitHub Actions
- Docker

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/AnujCh07ML/biological-age-prediction.git

cd biological-age-prediction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt

pip install -e .
```

Run the training pipeline

```bash
python main.py
```

---

# 📌 Current Status

## ✅ Completed

- NHANES multi-cycle data ingestion
- Data harmonization
- Modular preprocessing pipeline
- Feature engineering
- Random Forest benchmark
- XGBoost hyperparameter optimization
- LightGBM hyperparameter optimization
- SHAP explainability
- Final production model selection
- Model versioning
- Automated testing
- Docker environment
- GitHub Actions CI pipeline

## 🚧 Planned

- FastAPI inference service
- Cloud deployment
- Model monitoring
- External validation dataset
- Biological age proxy development

---

# 👤 Author

**Anuj Chauhan**

Machine Learning • Bioinformatics • Explainable AI

Interested in applying machine learning to computational biology, aging research, and biomedical data science.

---

# 📄 License

This project is licensed under the **MIT License**.
