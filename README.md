# 🧬 Biological Age Prediction (NHANES-Based)

A scalable machine learning pipeline to estimate **biological age** using multi-year NHANES health data.

---

## 🚀 Project Overview

This project focuses on modeling biological aging using clinical and biomarker data by:

- Integrating multiple NHANES cycles (2011–2020)
- Handling inconsistent feature availability across years
- Building a clean, modular, and reproducible ML pipeline

---

## 🧠 Key Focus

- End-to-end ML pipeline design
- Robust multi-table merging using **SEQN (unique identifier)**
- Feature engineering from heterogeneous biomedical data
- Model evaluation and interpretability using SHAP

---

## 🏗️ Project Structure

```
src/
  data/           # data loading & merging
  preprocessing/  # cleaning & transformations
  features/       # feature engineering
  models/         # training logic
  evaluation/     # metrics & validation
  interpret/      # SHAP analysis
  utils/          # helper functions

notebooks/        # experiments & exploration
data/             # raw & processed (git-ignored)
outputs/          # metrics, plots, model outputs
tests/            # unit tests
```

---

## 🔄 Pipeline

```
load_data
  → merge_data
  → combine_years
  → create_datasets
  → preprocess
  → train
  → evaluate
  → interpret
```

---

## 🧪 Experimental Extensions

Some biomarkers are not consistently available across all NHANES cycles.

To handle this, the pipeline supports **modular dataset configurations**:

- Optional inclusion of specific biomarkers (e.g., inflammation markers)
- Subset-based modeling without breaking the core pipeline

This enables **controlled experiments while preserving data integrity**.

---

## 📊 Outputs

- Model performance metrics (MAE, R²)
- Feature importance visualizations
- SHAP summary plots for interpretability

---

## ⚠️ Design Principles

- Single unified pipeline (no duplication)
- Dataset variations handled via configuration
- No biologically invalid imputations
- Reproducibility via Docker and environment setup

---

## 📌 Current Status

- [x] Data loading pipeline (NHANES XPT files)
- [x] Multi-year dataset merging
- [x] Modular project structure (`src/` based)
- [x] Dataset design (multi-configuration support)
- [ ] Feature engineering (in progress)
- [ ] Model training
- [ ] Evaluation & comparison
- [ ] SHAP interpretability

---

## 🧰 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost _(planned)_
- SHAP _(planned)_

---

## 🔁 Reproducibility

```bash
git clone https://github.com/AnujCh07ML/biological-age-prediction.git
cd biological-age-prediction

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

---

## 🔭 Future Work

- Define and validate biological age proxy
- Compare feature subsets (e.g., with vs without specific biomarkers)
- Add SHAP-based interpretation
- Optimize model performance
- API deployment for inference

---

## 🧠 Author Note

This project is designed as a **research-oriented ML system**, emphasizing:

- clean architecture
- biological validity
- extensibility for experimentation

---

## 📄 License

This project is licensed under the MIT License.
