from pathlib import Path
from functions.bruteforce_itertools import main_itertools

if __name__ == "__main__":
    home = Path("__file__").parents[0]
    data_folder = home / "data"
    data = data_folder.joinpath("dataset0.csv")
    main_itertools(500,data)
