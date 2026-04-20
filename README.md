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

## 📁 Project Structure

```text
biological-age-prediction/
├── data/                # Raw, interim, and processed datasets
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/           # Exploratory and debug notebooks
├── outputs/             # Metrics, plots, and reports
├── src/
│   └── biological_age/  # Core package
│       ├── data/            # Data loading & dataset creation
│       ├── preprocessing/   # Cleaning & transformations
│       ├── features/        # Feature engineering
│       ├── models/          # Training & stacking
│       ├── evaluation/      # Metrics & validation
│       ├── interpret/       # Explainability (SHAP)
│       ├── split/           # Train-test splitting
│       └── utils/           # Config & helper utilities
├── tests/               # Unit tests
├── main.py              # Pipeline entry point
├── config.yaml          # Configuration file
├── setup.py             # Package configuration
└── README.md
```

---

## 🏗️ Project Architecture

This project follows a **production-style Python package structure** to ensure consistency, reproducibility, and clean separation of concerns.

### 📦 Package Layout

The core codebase is organized under a `src/` directory with a dedicated package:

```
src/
└── biological_age/
    ├── data/
    ├── preprocessing/
    ├── features/
    ├── models/
    ├── evaluation/
    ├── interpret/
    ├── split/
    └── utils/
```

### 🔑 Key Design Decisions

#### 1. `src/`-based structure

All source code is placed under `src/` to avoid import conflicts and ensure that only explicitly installed packages are used.

#### 2. Dedicated package namespace (`biological_age`)

Instead of importing from ambiguous paths like `src.data`, the project exposes a clear package:

```python
from biological_age.data.load_data import load_all_data
```

This makes the code:

- more readable
- easier to reuse
- consistent across environments

#### 3. Installable project (`pip install -e .`)

The project is configured as an installable package using `setup.py`, enabling:

- consistent imports across Jupyter, scripts, and tests
- no need for `sys.path` hacks
- environment-independent execution

#### 4. Separation of concerns

Each module has a clear responsibility:

| Module           | Responsibility                       |
| ---------------- | ------------------------------------ |
| `data/`          | Data loading and dataset creation    |
| `preprocessing/` | Cleaning and transformation          |
| `features/`      | Feature engineering                  |
| `models/`        | Training and model definitions       |
| `evaluation/`    | Metrics and validation               |
| `interpret/`     | Model explainability (e.g., SHAP)    |
| `split/`         | Train-test splitting                 |
| `utils/`         | Shared utilities and config handling |

### 🚀 Why this matters

This structure ensures:

- reproducibility across environments (Jupyter, CLI, CI)
- scalability for adding new models or datasets
- clean integration with testing and deployment pipelines
- alignment with industry-standard ML project design

In short, the project is structured not just as a collection of scripts, but as a **maintainable and extensible ML system**.

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
