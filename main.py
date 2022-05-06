import cProfile
from functions.utils import extract_data
from functions.bruteforce_itertools import main_itertools
from functions.bruteforce import main_bruteforce_hm
from functions.opti_greedy import main_greedy1, main_greedy2
from functions.opti_knapsack import main_dynamique
from memory_profiler import profile

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


@profile
def main_set_0_BF_itertools():
    main_itertools(500, "E:\L7\Livrable\dataset0.csv")


@profile
def main_set_0_BF_HM():
    main_bruteforce_hm(500, "E:\L7\Livrable\dataset0.csv")


@profile
def main_set_0_opti_greedy1():
    main_greedy1(500, "E:\L7\Livrable\dataset0.csv")


@profile
def main_set_0_opti_greedy2():
    main_greedy2(500, "E:\L7\Livrable\dataset0.csv")


@profile
def main_set_0_opti_dynamique():
    main_dynamique(500, "E:\L7\Livrable\dataset0.csv")


@profile
def main_set_1_opti_greedy1():
    main_greedy1(500, "E:\L7\Livrable\dataset1_Python+P7.csv")


@profile
def main_set_1_opti_greedy2():
    main_greedy2(500, "E:\L7\Livrable\dataset1_Python+P7.csv")


@profile
def main_set_1_opti_dynamique():
    main_dynamique(500, "E:\L7\Livrable\dataset1_Python+P7.csv")


@profile
def main_set_2_opti_greedy1():
    main_greedy1(500, "E:\L7\Livrable\dataset2_Python+P7.csv")


@profile
def main_set_2_opti_greedy2():
    main_greedy2(500, "E:\L7\Livrable\dataset2_Python+P7.csv")


@profile
def main_set_2_opti_dynamique():
    main_dynamique(500, "E:\L7\Livrable\dataset2_Python+P7.csv")


if __name__ == "__main__":
    main_set_0_BF_itertools()
    main_set_0_opti_dynamique()
