from pathlib import Path
from functions.opti_greedy import main_greedy
from functions.opti_knapsack import main_dynamique

if __name__ == "__main__":
    home = Path("__file__").parents[0]
    data_folder = home / "data"
    data1 = data_folder.joinpath("dataset1_Python+P7.csv")
    data2 = data_folder.joinpath("dataset2_Python+P7.csv")
    """ print("\n---- Data set 1 ----\n")
    main_greedy(500,data1)
    main_dynamique(500,data1) """
    print("\n ---- Data set 2 ----\n")
    """ main_greedy(500,data2) """
    main_dynamique(500,data2)