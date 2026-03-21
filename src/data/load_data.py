import pandas as pd
from pathlib import Path


def load_xpt_file(file_path: Path) -> pd.DataFrame:
    """
    Load an XPT file into a pandas DataFrame.

    Parameters:
    file_path (Path): The path to the XPT file.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    return pd.read_sas(file_path, format='xport')


def load_year_data(year_path: Path) -> dict:
    """
    Load all XPT files for a given year into a dictionary of DataFrames.

    Parameters:
    year_path (Path): The path to the directory containing the year's XPT files.

    Returns:
    dict: A dictionary where keys are file names (without extension) and values are DataFrames.
    """
    data = {}
    for file in year_path.glob('*.xpt'):
        name = file.stem.split('_')[0]  # DEMO, CBC, etc.
        data[name] = load_xpt_file(file)

    return data
