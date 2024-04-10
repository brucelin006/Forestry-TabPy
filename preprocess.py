"""
Authors: Gaici Lin, Gia Ky Huynh
"""

import os
import re
import pandas as pd


def preprocess_data(filepath: str) -> str:
    # Get file name and define the output file name, e.g.live_trees_1705681447.csv -> live_tress.csv
    base_name: str = os.path.basename(filepath)
    print("==========", base_name, "==========")
    match = re.match(r"(.+?)_\d+\.csv$", base_name)
    output_filename = match.group(1) if match else ""

    # Load the dataset
    df = pd.read_csv(filepath)

    # Filter columns to exclude those ending with specific keywords that may affect the analysis
    selected_columns = [
        col
        for col in df.columns
        if not col.lower().endswith("limit") and not col.endswith("Class")
    ]
    selected_df = df[selected_columns]

    # Check the count of null values in each column
    null_counts = selected_df.isnull().sum()

    print("Found # of null values: ", null_counts[null_counts > 0], end="\n")
    print(selected_df.info(), "\n")

    export_filename = output_filename + ".csv"

    # Export the clean data as csv
    selected_df.to_csv(export_filename, index=False)

    return export_filename
