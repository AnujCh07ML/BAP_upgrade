# 🧬 Biological Age Prediction using NHANES Data

## Overview

This project aims to predict **biological age** using clinical biomarkers from the NHANES dataset.

Unlike chronological age, biological age reflects the physiological condition of an individual. This project explores whether **inflammation markers (CRP)** improve the accuracy of biological age prediction models.

---

## Problem Statement

Chronological age alone is not a reliable indicator of health and aging.

This project investigates:

* Can machine learning models estimate biological age from biomarkers?
* Does including inflammation (CRP) improve prediction performance?

---

## Key Idea

Two datasets are created to enable a controlled comparison:

* **Dataset A (No CRP):**

  * Uses all available years
  * Excludes inflammation marker
* **Dataset B (With CRP):**

  * Uses only rows where CRP is available
  * Includes inflammation marker

This allows a **research-style comparison** of model performance.

---

## Pipeline

```
Raw NHANES Data (.xpt)
→ Data Loading (SAS parsing)
→ Merge Across Years
→ Feature Engineering
→ Dataset Creation (CRP vs No CRP)
→ Model Training
→ Evaluation
→ SHAP Interpretation
```

---

## Project Structure

```
src/
  data/           # data loading & merging
  preprocessing/  # cleaning & transformations
  features/       # feature engineering
  models/         # training logic
  evaluation/     # metrics
  interpret/      # SHAP analysis
  utils/          # helper functions

notebooks/        # experimentation
data/             # raw & processed (ignored in git)
outputs/          # plots & results
tests/            # unit tests
```

---

## Current Status

* [x] Data loading pipeline (XPT files)
* [x] Multi-year dataset merging
* [x] Modular project structure (src-based)
* [x] Dataset design (CRP vs No CRP)
* [ ] Feature engineering (in progress)
* [ ] Model training
* [ ] Evaluation & comparison
* [ ] SHAP interpretability

---

## Tech Stack

* Python
* Pandas / NumPy
* Scikit-learn
* XGBoost (planned)
* SHAP (planned)

---

## Reproducibility

```bash
git clone https://github.com/AnujCh07ML/biological-age-prediction.git
cd biological-age-prediction

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

---

## Future Work

* Implement biological age proxy
* Compare models with and without CRP
* Add SHAP-based feature interpretation
* Optimize model performance
* API deployment

---

## License

This project is licensed under the MIT License.
