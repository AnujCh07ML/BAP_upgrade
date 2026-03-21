import pandas as pd


def merge_year_data(year_data: dict) -> pd.DataFrame:
    dfs = list(year_data.values())

    df_merged = dfs[0]

    for df in dfs[1:]:
        df_merged = df_merged.merge(df, on='SEQN', how='inner')

    return df_merged
