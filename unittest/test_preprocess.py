# test_preprocess.py
"""
Authors: Gia Ky Huynh, Gaici Lin
"""

import os
import pandas as pd
import pytest
from preprocess import preprocess_data


# Fixture to create a temporary CSV file for testing
@pytest.fixture
def temp_csv(tmp_path):
    data = {"Column1": [1, 2, 3], "someClass": [4, 5, 6], "tempLimit": [7, 8, 9]}
    df = pd.DataFrame(data)
    file_path = (
        tmp_path / "test_data_123456.csv"
    )  # appending "test_data_123456.csv" to tmp_path
    df.to_csv(file_path, index=False)
    return str(file_path), "test_data.csv"


# Test case for checking the output filename
def test_output_filename(temp_csv):
    file_path, expected_filename = temp_csv
    output_filename = preprocess_data(file_path)
    assert (
        output_filename == expected_filename
    ), f"Expected filename {expected_filename}, but got {output_filename}"


# Test case for verifying column filtering
def test_column_filtering(temp_csv):
    file_path, _ = temp_csv
    output_filename = preprocess_data(file_path)
    df = pd.read_csv(output_filename)

    # Check that the 'LimitClass' column is removed and 'Column1', 'AnotherColumn' remain
    assert "someClass" not in df.columns
    assert "tempLimit" not in df.columns
    assert "Column1" in df.columns

    # Cleanup the output file
    os.remove(output_filename)
