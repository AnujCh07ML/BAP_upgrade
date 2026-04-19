import pandas as pd


def split_features(df: pd.DataFrame):
    """
    Split dataset into numerical and categorical columns.
    """

    numerical_cols = df.select_dtypes(
        include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    return numerical_cols, categorical_cols


def impute_missing_values(df: pd.DataFrame, numerical_cols, categorical_cols):
    """
    Handle missing values.
    """

    df = df.copy()

    # Numerical → median
    for col in numerical_cols:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)

    # Categorical → mode
    for col in categorical_cols:
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)

    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full preprocessing pipeline.
    """

    print(f"Before preprocessing: {df.shape}")

    # Step 1: Split features
    numerical_cols, categorical_cols = split_features(df)

    print(f"Numerical columns: {len(numerical_cols)}")
    print(f"Categorical columns: {len(categorical_cols)}")

    # Step 2: Handle missing values
    df = impute_missing_values(df, numerical_cols, categorical_cols)

    print(f"After preprocessing: {df.shape}")

    return df
