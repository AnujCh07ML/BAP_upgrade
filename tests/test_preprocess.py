import pandas as pd
from sklearn.compose import ColumnTransformer

from biological_age.preprocessing.preprocess import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    build_preprocessor,
    split_features_target,
)


def test_build_preprocessor_returns_column_transformer():
    """
    Verify that build_preprocessor()
    returns a ColumnTransformer.
    """
    preprocessor = build_preprocessor()

    assert isinstance(
        preprocessor,
        ColumnTransformer,
    )


def test_split_features_target():
    """
    Verify X and y are split correctly.
    """
    data = {}

    for col in FEATURE_COLUMNS:
        data[col] = [1, 2]

    data[TARGET_COLUMN] = [30, 40]

    df = pd.DataFrame(data)

    X, y = split_features_target(df)

    assert list(X.columns) == FEATURE_COLUMNS
    assert y.name == TARGET_COLUMN
    assert len(X) == 2
    assert len(y) == 2


def test_target_not_in_features():
    """
    Verify target column is not
    included in feature matrix.
    """
    data = {}

    for col in FEATURE_COLUMNS:
        data[col] = [1]

    data[TARGET_COLUMN] = [30]

    df = pd.DataFrame(data)

    X, y = split_features_target(df)

    assert TARGET_COLUMN not in X.columns
