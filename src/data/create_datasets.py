import pandas as pd


def drop_high_missing_columns(df: pd.DataFrame, threshold: float = 0.8) -> pd.DataFrame:
    """
    Drop columns with missing values above threshold.

    Args:
        df: Input dataframe
        threshold: max allowed missing ratio (default 80%)

    Returns:
        Cleaned dataframe
    """
    missing_ratio = df.isna().mean()

    valid_cols = missing_ratio[missing_ratio < threshold].index

    df_clean = df[valid_cols]

    return df_clean


def create_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main dataset creation pipeline.
    """

    # Step 1: Drop high-missing columns
    df_clean = drop_high_missing_columns(df, threshold=0.8)

    return df_clean
