from typing import Dict, Tuple
import pandas as pd


def merge_features_for_year(
    data: Dict[Tuple[str, str], pd.DataFrame],
    year: str
) -> pd.DataFrame:
    """
    Merge all feature tables for a given year using SEQN.

    Parameters:
        data: dict with keys (year, feature) -> DataFrame
        year: year to process

    Returns:
        Merged DataFrame for that year
    """

    # READ: DEMO is the base table (contains core demographic + SEQN)
    if (year, "DEMO") not in data:
        raise ValueError(f"Missing DEMO data for year {year}")

    df_merged = data[(year, "DEMO")].copy()

    # READ: only loop through features available for THIS year
    year_features = [f for (y, f) in data.keys() if y == year]

    for feature in year_features:

        if feature == "DEMO":
            continue

        df_feature = data[(year, feature)]

        # READ: SEQN is required to merge individuals across datasets
        if "SEQN" not in df_feature.columns:
            raise ValueError(f"SEQN missing in {feature} for {year}")

        # READ: avoid duplicate 'year' column during merge
        df_feature = df_feature.drop(columns=["year"], errors="ignore")

        # READ: left join keeps all individuals from DEMO
        df_merged = pd.merge(
            df_merged,
            df_feature,
            on="SEQN",
            how="left"
        )

    return df_merged


def merge_all_years(
    data: Dict[Tuple[str, str], pd.DataFrame]
) -> Dict[str, pd.DataFrame]:
    """
    Merge features for all years.

    Returns:
        dict: year -> merged DataFrame
    """

    # READ: sorted ensures deterministic order (important for reproducibility)
    years = sorted({k[0] for k in data.keys()})

    merged_data = {}

    for year in years:
        merged_data[year] = merge_features_for_year(data, year)

    return merged_data


def combine_years(
    merged_data: Dict[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    Combine all yearly datasets into a single DataFrame.

    Returns:
        Single concatenated DataFrame
    """

    dfs = []

    for year, df in merged_data.items():

        # READ: assign year column safely (no mutation issues)
        df_with_year = df.assign(year=year)

        dfs.append(df_with_year)

    return pd.concat(dfs, ignore_index=True)
