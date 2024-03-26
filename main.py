import pandas as pd

PATH_TO_LIVE_TREES = "live_trees_1705681447.csv"


# Load dataset
df = pd.read_csv(PATH_TO_LIVE_TREES)
# Filter columns: Exclude columns that end with 'Key' or 'Code'
filtered_columns = [
    col
    for col in df.columns
    if not col.endswith("Key")
    and not col.endswith("Code")
    and not col.lower().endswith("limit")
    and not col.endswith("Class")
]
# Calculate correlations
corr_matrix = df[filtered_columns].corr(numeric_only=True)
# Flatten the Correlation Matrix
corr_series = corr_matrix.unstack()
# Remove Self-Correlations
corr_series = corr_series[
    corr_series.index.get_level_values(0) != corr_series.index.get_level_values(1)
]
# Sort by Absolute Values
sorted_series = corr_series.abs().sort_values(ascending=False).drop_duplicates()
# Discard correlations with coefficient of 1 and get the first 3 results
strong_corr_columns = sorted_series.head(5)
print("==========strong_corr_columns==========")
print(strong_corr_columns)
print()

# Extract unique column names from the pairs
unique_columns = set()
for pair in strong_corr_columns.keys():
    unique_columns.update(pair)
print("==========unique_columns==========")
print(unique_columns)
print()

strong_corr_df = df[list(unique_columns)]
print("==========strong_corr_df==========")
print(strong_corr_df.head())
print()

print("==========strong_corr_df null values==========")
print(strong_corr_df.isna().sum())
print()
