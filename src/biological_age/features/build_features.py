"""
Feature engineering module.

Creates biologically meaningful engineered features that can be
used consistently during training and inference.
"""

import numpy as np
import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create engineered features.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing selected modeling features.

    Returns
    -------
    pd.DataFrame
        Dataframe with engineered features.
    """

    df = df.copy()

    # =====================================
    # Kidney Function
    # =====================================

    df["bun_creatinine_ratio"] = np.where(
        df["creatinine"] > 0,
        df["blood_urea_nitrogen"] / df["creatinine"],
        np.nan,
    )

    # =====================================
    # Liver Function
    # =====================================

    df["albumin_globulin_ratio"] = np.where(
        df["globulin"] > 0,
        df["albumin"] / df["globulin"],
        np.nan,
    )

    # =====================================
    # Lipid Profile
    # =====================================

    df["cholesterol_hdl_ratio"] = np.where(
        df["hdl_cholesterol"] > 0,
        df["total_cholesterol"] / df["hdl_cholesterol"],
        np.nan,
    )

    # =====================================
    # Triglyceride-to-HDL Cholesterol Ratio (TG/HDL)
    # Associated with insulin resistance and metabolic health.
    # =====================================
    df["triglyceride_hdl_ratio"] = np.where(
        df["hdl_cholesterol"] > 0,
        df["triglycerides"] / df["hdl_cholesterol"],
        np.nan,
    )

    return df
