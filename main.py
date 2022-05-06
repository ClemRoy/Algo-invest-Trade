from operator import le
from functions.utils import extract_data
from functions.bruteforce_itertools import main_itertools
from functions.bruteforce import main_bruteforce_hm
from functions.opti_greedy import main_greedy1, main_greedy2
from functions.opti_knapsack import main_dynamique

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


def main(data_path: str):
    data_length = len(extract_data(data_path))
    if data_length <= 25:
        print("\n ---- Bruteforce Itertools: ----\n")
        main_itertools(500, data_path)
        print("\n ----Bruteforce HM: ----\n")
        main_bruteforce_hm(500, data_path)
        print("\n ----Opti Greedy 1: ----\n")
        main_greedy1(500, data_path)
        print("\n ----Opti Greedy 2: ----\n")
        main_greedy2(500, data_path)
        print("\n ----Opti Dynamique 1: ----\n")
        main_dynamique(500, data_path)
    else:
        print("\n ----Opti Greedy 1: ----\n")
        main_greedy1(500, data_path)
        print("\n ----Opti Greedy 2: ----\n")
        main_greedy2(500, data_path)
        print("\n ----Opti Dynamique 1: ----\n")
        main_dynamique(500, data_path)


if __name__ == "__main__":
    main("E:\L7\Livrable\dataset1_Python+P7.csv")
