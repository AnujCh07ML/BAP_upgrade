from pathlib import Path
import pandas as pd

from src.data.load_data import load_year_data
from src.data.merge_data import merge_year_data


RAW_DIR = Path('data/raw')
INTERIM_DIR = Path('data/interim')


def process_all_years():
    all_years = []

    for year_path in RAW_DIR.iterdir():
        if year_path.is_dir():
            print(f"Processing {year_path.name}")

            data_dict = load_year_data(year_path)
            merged_df = merge_year_data(data_dict)

            merged_df['year'] = year_path.name

            all_years.append(merged_df)

    final_df = pd.concat(all_years, axis=0)

    return final_df


def save_interim(df: pd.DataFrame):
    INTERIM_DIR.mkdir(parents=True, exist_ok=True)

    output_path = INTERIM_DIR / "nhanes_merged.parquet"
    df.to_parquet(output_path, index=False)

    print(f"Saved to {output_path}")


if __name__ == "__main__":
    df = process_all_years()
    save_interim(df)
