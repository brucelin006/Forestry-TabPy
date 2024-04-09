"""
Authors: Gaici Lin, Gia Ky Huynh
"""

import os
import re
import pandas as pd


def preprocess_data(filepath: str, selected_columns: list[str]) -> str:
    # Get file name and define the output file name, e.g.live_trees_1705681447.csv -> live_tress.csv
    base_name: str = os.path.basename(filepath)
    print("==========", base_name, "==========")
    match = re.match(r"(.+?)_\d+\.csv$", base_name)
    output_filename = match.group(1) if match else ""

    # Load the dataset
    df = pd.read_csv(filepath)

    selected_df = df[selected_columns]

    # Check the count of null values in each column
    null_counts = selected_df.isnull().sum()

    print("Found # of null values: ", null_counts[null_counts > 0], end="\n")

    cleaned_df = selected_df.dropna()
    print(cleaned_df.info(), "\n")

    export_filename = output_filename + ".csv"

    # Export the clean data as csv
    cleaned_df.to_csv(export_filename, index=False)

    return export_filename
