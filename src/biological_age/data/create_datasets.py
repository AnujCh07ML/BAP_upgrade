import pandas as pd


def drop_high_missing_columns(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Drop columns with missing ratio above threshold.
    """

    valid_cols = []

    for col in df.columns:
        missing_ratio = df[col].isna().mean()

        if missing_ratio < threshold:
            valid_cols.append(col)

    return df[valid_cols]


def create_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main dataset creation pipeline.
    """

    print(f"Original shape: {df.shape}")

    # Step 1: Remove very high-missing columns (>60%)
    df_clean = drop_high_missing_columns(df, threshold=0.6)

    print(f"After dropping >60% missing: {df_clean.shape}")

    # Step 2: Remove moderately bad columns (>40%)
    df_clean = drop_high_missing_columns(df_clean, threshold=0.4)

    print(f"After dropping >40% missing: {df_clean.shape}")

    return df_clean
