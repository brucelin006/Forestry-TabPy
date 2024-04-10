# test_analysis.py
import os
import pandas as pd
import pytest
from analysis import (
    load_dataset,
    filter_columns,
    calculate_correlations,
    extract_strong_correlations,
    extract_unique_columns,
)


@pytest.fixture
def sample_data():
    """Fixture to create a simple dataframe for testing."""
    data = {
        "PlotKey": [1, 2],
        "PlotName": ["Plot A", "Plot B"],
        "TreeKey": [10, 20],
        "SpeciesCode": ["SPEC1", "SPEC2"],
        "SoundWoodLength": [10.5, 11.0],
        "OfficeRingCount": [15, 16],
    }
    df = pd.DataFrame(data)
    filename = "test_data.csv"
    df.to_csv(filename, index=False)

    yield filename

    # remove the file created
    os.remove(filename)


def test_load_dataset(sample_data):
    df = load_dataset(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_filter_columns(sample_data):
    df = load_dataset(sample_data)
    filtered_columns = filter_columns(df)
    assert "PlotKey" not in filtered_columns
    assert "PlotName" in filtered_columns
    assert "TreeKey" not in filtered_columns
    assert "SpeciesCode" not in filtered_columns
    assert "SoundWoodLength" in filtered_columns
    assert "OfficeRingCount" in filtered_columns


def test_calculate_correlations(sample_data):
    df = load_dataset(sample_data)
    filtered_columns = filter_columns(df)
    sorted_series = calculate_correlations(df, filtered_columns)
    assert not sorted_series.empty
    assert all(
        sorted_series.index.get_level_values(0)
        != sorted_series.index.get_level_values(1)
    )


def test_extract_strong_correlations(sample_data):
    df = load_dataset(sample_data)
    filtered_columns = filter_columns(df)
    sorted_series = calculate_correlations(df, filtered_columns)
    strong_corr_columns = extract_strong_correlations(sorted_series, num_results=2)
    assert len(strong_corr_columns) <= 2


def test_extract_unique_columns(sample_data):
    df = load_dataset(sample_data)
    filtered_columns = filter_columns(df)
    sorted_series = calculate_correlations(df, filtered_columns)
    strong_corr_columns = extract_strong_correlations(sorted_series, num_results=2)
    unique_columns = extract_unique_columns(strong_corr_columns)
    assert isinstance(unique_columns, set)
    assert len(unique_columns) > 0
