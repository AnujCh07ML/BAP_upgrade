from pathlib import Path
import pandas as pd


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


def read_xpt(file: Path) -> pd.DataFrame:
    """
    Read .xpt file safely.
    """
    return pd.read_sas(file, format="xport", encoding="latin1")


def load_all_data(base_path: Path) -> dict:
    data = {}

    for year_folder in base_path.iterdir():
        if not year_folder.is_dir():
            continue

        year = year_folder.name

        for file in year_folder.glob('*.xpt'):
            dataset_name = extract_name(file)

            try:
                df = read_xpt(file)

                if 'year' not in df.columns:
                    df["year"] = year

                # flat dictionary using tuple key
                key = (year, dataset_name)
                data[key] = df

            except Exception as e:
                print(f'Error reading {file}: {e}')
                continue

    return data
