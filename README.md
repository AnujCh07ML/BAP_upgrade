# 🧬 Biological Age Prediction using NHANES Data

## 📌 Overview

This project focuses on predicting **biological age** using clinical and biochemical data from the NHANES dataset.

The long-term goal is to build a system that enables:

- Understanding how biological signals relate to aging
- Running experiments on biomarkers (e.g., inflammation)
- Exploring interventions that may influence aging trajectories

This project is designed as a **research-oriented ML pipeline**, not just a model.

---

## 🎯 Objectives

- Build a scalable ML pipeline for biological age prediction
- Compare models **with vs without inflammation markers (CRP)**
- Identify key biological features influencing aging
- Enable future experimentation in **epigenetics and longevity research**

---

## 🧠 Key Idea

We construct **two dataset variants**:

| Model              | Data Used              | Features               |
| ------------------ | ---------------------- | ---------------------- |
| Base Model         | All years              | No inflammation marker |
| Inflammation Model | Subset (CRP available) | Includes CRP           |

This allows us to answer:

> Does inflammation significantly improve biological age prediction?

---

## 🏗️ Project Structure

```
.
├── src/
│   ├── data/              # Data loading & dataset creation
│   ├── preprocessing/     # Cleaning & transformations
│   ├── features/          # Feature engineering
│   ├── models/            # Model training
│   ├── evaluation/        # Metrics & validation
│   ├── interpret/         # SHAP analysis
│   └── utils/
│
├── data/
│   ├── raw/               # Original NHANES data
│   └── processed/         # Clean datasets
│
├── models/                # Saved trained models
├── outputs/               # Plots, metrics, reports
├── notebooks/             # Exploratory analysis
├── tests/                 # Unit tests
│
├── config.yaml
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline

```
load_data → merge_data → combine_years → create_datasets → preprocess → train → evaluate → interpret
```

---

## 📊 Features Used

- Demographics (age, gender, etc.)
- Blood biomarkers
- Clinical measurements
- Inflammation marker (CRP) _(in selected model)_

---

## 🤖 Models

- Random Forest
- XGBoost
- Stacking / Ensemble models

---

## 📈 Evaluation Metrics

- Mean Absolute Error (MAE)
- R² Score

Outputs are stored in:

```
outputs/
├── metrics.json
├── feature_importance.png
└── shap_summary.png
```

---

## 🔍 Interpretability

We use **SHAP (SHapley Additive Explanations)** to:

- Identify key aging biomarkers
- Understand model behavior
- Support biological insights

---

## 🧪 Research Direction

This project is being developed as a foundation for:

- Epigenetic aging models
- Biomarker-based interventions
- Longevity research

Future work includes:

- DNA methylation data integration
- Time-series biomarker tracking
- Intervention simulation

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run pipeline

```
python main.py
```

---

## 🐳 Docker Support

```
docker build -t biological-age .
docker run biological-age
```

---

## 📌 Why This Project Matters

Most ML projects focus only on prediction.

This project focuses on:

- **Scientific understanding**
- **Reproducible pipelines**
- **Real-world biological impact**

---

## 👤 Author

ANuj

- Machine Learning & Bioinformatics
- Focus: Aging, Epigenetics, Longevity

---

## 🌍 Goal

To contribute to research enabling:

> Radical life extension and deeper understanding of human biology.
