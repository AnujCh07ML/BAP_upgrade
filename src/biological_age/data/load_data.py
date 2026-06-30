from pathlib import Path
import pandas as pd

from biological_age.utils.config import (
    PROJECT_ROOT,
    load_config,
)


def clean_invalid_numeric_values(
    df: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    """
    Replace invalid near-zero values with NaN.

    Some NHANES SAS imports contain corrupted
    pseudo-missing values like 5.397605e-79.
    """

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    invalid_mask = (
        df[numeric_cols].abs() < threshold
    )

    invalid_count = invalid_mask.sum().sum()

    df[numeric_cols] = df[numeric_cols].mask(
        invalid_mask
    )

    print(
        f"[INFO] Replaced "
        f"{invalid_count} invalid values."
    )

    return df


def extract_name(file: Path) -> str:
    """
    Extract dataset name from file name.
    Handles:
    P_DEMO.xpt → DEMO
    DEMO_G.xpt → DEMO
    """
    parts = file.stem.split("_")

    if parts[0] == "P":
        return parts[1]
    return parts[0]


def read_xpt(file: Path, threshold: float,) -> pd.DataFrame:
    """
    Read .xpt file safely.
    """
    df = pd.read_sas(file, format="xport", encoding="latin1",)

    df = clean_invalid_numeric_values(df, threshold=threshold,)

    return df


def load_all_data(base_path: Path, threshold: float,) -> dict:
    data = {}

    for year_folder in base_path.iterdir():
        if not year_folder.is_dir():
            continue

        year = year_folder.name

        for file in year_folder.glob('*.xpt'):
            dataset_name = extract_name(file)

            try:
                df = read_xpt(file, threshold=threshold,)

                if 'year' not in df.columns:
                    df["year"] = year

                # flat dictionary using tuple key
                key = (year, dataset_name)
                data[key] = df

            except Exception as e:
                print(f'Error reading {file}: {e}')
                continue

    return data


...


def load_processed_dataset() -> pd.DataFrame:
    """
    Load the processed dataset defined in config.yaml.

    Returns
    -------
    pd.DataFrame
        Loaded processed dataset.
    """
    config = load_config()

    dataset_path = PROJECT_ROOT / config["paths"]["processed"]

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Processed dataset not found: {dataset_path}"
        )

    return pd.read_parquet(dataset_path)
