import pandas as pd
import pytest

from biological_age.features.feature_selection import (
    KEEP_COLUMNS,
    select_features,
)


def _make_input_df() -> pd.DataFrame:
    data = {
        column: [1.0, 2.0]
        for column in KEEP_COLUMNS
    }

    # Extra column that should be removed
    data["extra_column"] = [99.0, 100.0]

    return pd.DataFrame(data)


def test_select_features_returns_expected_columns():
    df = _make_input_df()

    result = select_features(df)

    assert list(result.columns) == KEEP_COLUMNS
    assert "extra_column" not in result.columns


def test_select_features_raises_for_missing_columns():
    df = _make_input_df().drop(columns=["albumin"])

    with pytest.raises(ValueError, match="Missing features"):
        select_features(df)
