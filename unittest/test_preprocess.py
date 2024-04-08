"""
Authors: Gia Ky Huynh, Gaici Lin
"""

import pytest
import pandas as pd

from preprocess import preprocess_data


def test_preprocess_data_successfully_drop_null_values():
    # Normal case should drop null value

    df_original = pd.read_csv("odd_trees_1705681447.csv")
    # Assert before run test that have 99 records
    assert len(df_original["SpeciesCode"]) == 99

    preprocess_data("odd_trees_1705681447.csv", ["SpeciesCode"])

    df = pd.read_csv("odd_trees.csv")
    # Assert after run test that have 97 records, dropped 2 null records
    assert len(df["SpeciesCode"]) == 97


def test_preprocess_data_raise_exception_when_file_is_not_exist():
    # Should raise ValueError for when file is not exist
    with pytest.raises(Exception):
        preprocess_data("not_exist_file.csv", ["SpeciesCode"])


def test_preprocess_data_raise_exception_when_column_is_not_exist():
    # Should raise ValueError for when column is not exist
    with pytest.raises(Exception):
        preprocess_data("odd_trees_1705681447.csv", ["Invalid_column"])
