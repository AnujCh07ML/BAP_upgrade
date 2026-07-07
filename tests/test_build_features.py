import numpy as np
import pandas as pd
import math
from typing import cast

from biological_age.features.build_features import build_features


def _make_input_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "blood_urea_nitrogen": [20.0, 15.0],
            "creatinine": [2.0, 0.0],
            "albumin": [5.0, 4.2],
            "globulin": [4.0, 0.0],
            "total_cholesterol": [200.0, 180.0],
            "hdl_cholesterol": [50.0, 0.0],
            "triglycerides": [100.0, 150.0],
            "sex": [1.0, 0.0],
            "age_years": [40.0, 55.0],
        }
    )


def test_build_features_creates_expected_ratios():
    df = _make_input_df()

    result = build_features(df)

    assert np.isclose(
        cast(float, result.at[0, "bun_creatinine_ratio"]),
        10.0,
    )

    assert np.isclose(
        cast(float, result.at[0, "albumin_globulin_ratio"]),
        1.25,
    )

    assert np.isclose(
        cast(float, result.at[0, "cholesterol_hdl_ratio"]),
        4.0,
    )

    assert np.isclose(
        cast(float, result.at[0, "triglyceride_hdl_ratio"]),
        2.0,
    )


def test_build_features_returns_nan_for_zero_denominators():
    df = _make_input_df()

    result = build_features(df)

    assert math.isnan(
        cast(float, result.at[1, "bun_creatinine_ratio"])
    )

    assert math.isnan(
        cast(float, result.at[1, "albumin_globulin_ratio"])
    )

    assert math.isnan(
        cast(float, result.at[1, "cholesterol_hdl_ratio"])
    )

    assert math.isnan(
        cast(float, result.at[1, "triglyceride_hdl_ratio"])
    )


def test_build_features_does_not_mutate_input_dataframe():
    df = _make_input_df()
    original = df.copy(deep=True)

    _ = build_features(df)

    pd.testing.assert_frame_equal(df, original)
    assert "bun_creatinine_ratio" not in df.columns
    assert "albumin_globulin_ratio" not in df.columns
    assert "cholesterol_hdl_ratio" not in df.columns
    assert "triglyceride_hdl_ratio" not in df.columns
