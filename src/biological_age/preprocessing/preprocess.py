from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from biological_age.features.feature_selection import (
    TARGET_COLUMN,
    NUMERIC_FEATURES,
    CATEGORICAL_FEATURES,
    FEATURE_COLUMNS,
)


# =====================================
# Numeric Preprocessing Pipeline
# =====================================

numeric_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median"),
    ),
    (
        "scaler",
        StandardScaler(),
    ),
])


# =====================================
# Categorical Preprocessing Pipeline
# =====================================

categorical_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(
            strategy="most_frequent",
        ),
    ),
])


# =====================================
# Full Preprocessor
# =====================================

def build_preprocessor():
    """
    Build the preprocessing pipeline for
    biological age prediction.

    Returns
    -------
    ColumnTransformer
        Preprocessing pipeline for numeric and
        categorical features.
    """

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                NUMERIC_FEATURES,
            ),
            (
                "categorical",
                categorical_pipeline,
                CATEGORICAL_FEATURES,
            ),
        ]
    )

    return preprocessor


# =====================================
# Feature / Target Split
# =====================================

def split_features_target(df):
    """
    Split dataframe into features (X)
    and target (y).

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.

    Returns
    -------
    tuple[pd.DataFrame, pd.Series]
        Feature matrix and target vector.
    """

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    return X, y
