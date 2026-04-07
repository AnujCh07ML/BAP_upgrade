import pandas as pd


def merge_year_data(year_data: dict) -> pd.DataFrame:

    # 1. Start from DEMO (base table)
    if "DEMO" not in year_data:
        raise ValueError("DEMO file missing — cannot proceed")

    merged_df = year_data["DEMO"]

    # 2. Merge all other datasets onto DEMO
    for name, df in year_data.items():
        if name == "DEMO":
            continue

        merged_df = merged_df.merge(df, on="SEQN", how="left")

    return merged_df
