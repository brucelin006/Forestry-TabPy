from analysis import analyze
from preprocess import preprocess_data

# The path of the source csv file that needs to be processed and plot onto Tableau
paths = ["live_trees_1705681447.csv", "odd_trees_1705681447.csv"]


def main():
    for path in paths:
        # preprocess the dataset
        if path.startswith("live_"):
            processed_file_path = preprocess_data(
                path,
                selected_columns=[
                    "PlotKey",
                    "TreeKey",
                    "SpeciesCode",
                    "DBH",
                    "TotalHeight",
                    "Age_BH",
                ],
            )
        elif path.startswith("odd_"):
            processed_file_path = preprocess_data(
                path,
                selected_columns=[
                    "PlotKey",
                    "TreeKey",
                    "SpeciesCode",
                    "DBH",
                    "TotalHeight",
                ],
            )
        else:
            raise FileNotFoundError("File not exists")
        # analyze the dataset
        analyze(processed_file_path)


if __name__ == "__main__":
    main()
