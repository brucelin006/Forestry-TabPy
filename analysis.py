"""
Authors: Gaici Lin, Gia Ky Huynh
"""

from pprint import pprint
import pandas as pd


def load_dataset(path):
    """Load the dataset from the given path."""
    return pd.read_csv(path)


def filter_columns(df):
    """Filter columns to exclude those ending with Key and Code, which may affect the analysis."""
    return [
        col
        for col in df.columns
        if not col.endswith("Key") and not col.endswith("Code")
    ]


def calculate_correlations(df, filtered_columns):
    """Calculate and sort correlations for the filtered columns."""
    # perform correlation on the filtered colimns
    corr_matrix = df[filtered_columns].corr(numeric_only=True)
    corr_series = corr_matrix.unstack()
    # get rid of self correlations
    corr_series = corr_series[
        corr_series.index.get_level_values(0) != corr_series.index.get_level_values(1)
    ]
    # sort by correlation coefficient in descending order and drop any duplicates
    sorted_series = corr_series.abs().sort_values(ascending=False).drop_duplicates()
    return sorted_series


def extract_strong_correlations(sorted_series, num_results=5):
    """Extract the top N strong correlations."""
    return sorted_series.head(num_results)


def extract_unique_columns(strong_corr_columns):
    """Extract unique column names from the strong correlation pairs."""
    unique_columns = set()
    for pair in strong_corr_columns.keys():
        unique_columns.update(pair)
    return unique_columns


def analyze(path_to_file):
    """Combine all the necessary steps to analyze the dataset and output results to the console"""
    # Load dataset
    df = load_dataset(path_to_file)
    # Filter out irrelavant or meaningless columns, for example columns that end with Key, Code
    filtered_columns = filter_columns(df)
    sorted_series = calculate_correlations(df, filtered_columns)
    # Get the columns that are strongly correlated
    strong_corr_columns = extract_strong_correlations(sorted_series)
    # Since correlation dataframe contains duplicate, remove them to just get columns that are strongly correlated
    unique_columns = extract_unique_columns(strong_corr_columns)

    # Display results
    print("========== Strong Correlation Columns ==========")
    print(strong_corr_columns.to_string())  # to_string for better formatting

    print("\n========== Unique Columns ==========")
    pprint(unique_columns)  # pprint for better set display

    print("\n==========strong_corr_df==========")
    strong_corr_df = df[list(unique_columns)]
    print(strong_corr_df.head())
    print()

    print("==========strong_corr_df null values==========")
    print(strong_corr_df.isna().sum())
    print()
