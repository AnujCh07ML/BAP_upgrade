# Final Production Model

## Model
XGBoost Regressor

## Version
v1.0.0

## Training Data
NHANES 2011–2020

## Features
31 total features
- 28 original biomarkers
- 3 engineered ratio features

## Engineered Features
- Albumin / Globulin Ratio
- Total Cholesterol / HDL Ratio
- Triglycerides / HDL Ratio

## Performance
| Metric | Value |
|--------|------:|
| MAE | 7.56 |
| RMSE | 10.67 |
| R² | 0.801 |

## Notes
This model was selected as the production model after evaluating the tuned baseline and the feature-engineered pipeline. The engineered features provided a measurable improvement and were validated with SHAP.
