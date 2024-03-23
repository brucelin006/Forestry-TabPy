import os
import re
from typing import NoReturn
import pandas as pd

PATH_TO_LIVE_TREES = "live_trees_1705681447.csv"
PATH_TO_ODD_TREES = "odd_trees_1705681447.csv"


def preprocess_data(filepath: str, selected_columns: list[str]) -> None:
    # Get file name and define the output file name
    base_name: str = os.path.basename(filepath)
    print("==========", base_name, "==========")
    match = re.match(r"(.+?)_\d+\.csv$", base_name)
    output_filename = match.group(1) if match else ""

    # Load the dataset
    df = pd.read_csv(filepath)

    selected_df = df[selected_columns]

    # # Check the count of null values in each column
    null_counts = selected_df.isnull().sum()
    print("Found # of null values: ", null_counts[null_counts > 0], end="\n")

    cleaned_df = selected_df.dropna()
    print(cleaned_df.info(), "\n")

    # # Export the clean data as csv
    cleaned_df.to_csv(output_filename + ".csv", index=False)


preprocess_data(
    PATH_TO_LIVE_TREES,
    ["PlotKey", "TreeKey", "SpeciesCode", "DBH", "TotalHeight", "Age_BH"],
)
preprocess_data(
    PATH_TO_ODD_TREES, ["PlotKey", "TreeKey", "SpeciesCode", "DBH", "TotalHeight"]
)
