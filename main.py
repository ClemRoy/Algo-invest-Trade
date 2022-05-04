import csv
from timeit import default_timer as timer
from functions.bruteforce import main_bruteforce_hm
from functions.bruteforce_itertools import main_itertools
from functions.opti_greedy import main_greedy1, main_greedy2
from functions.opti_knapsack import main_dynamique
# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e

data_set_0 = []
data_set_0_25 = []
data_set_1 = []
data_set_2 = []
data_set_4 = []





with open("E:\L7\dataset0.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        data_set_0.append(row)

with open("E:\L7\dataset0_25.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        data_set_0_25.append(row)

with open("E:\L7\dataset1_Python+P7.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        data_set_1.append(row)

with open("E:\L7\dataset2_Python+P7.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        data_set_2.append(row)

with open("E:\L7\dataset4.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        data_set_4.append(row)

print("set0 -- 20 actions")
print("bruteforce_itertools")
main_itertools(500,data_set_0)
print("bruteforce:")
main_bruteforce_hm(data_set_0)
print("greedy1:")
main_greedy1(500, data_set_0)
print("greedy2:")
main_greedy2(500, data_set_0)
print("dynamique:")
main_dynamique(500, data_set_0)

print("set0 -- 25 actions")
print("bruteforce_itertools")
main_itertools(500,data_set_0_25)
print("bruteforce:")
main_bruteforce_hm(data_set_0_25)
print("greedy1:")
main_greedy1(500, data_set_0_25)
print("greedy2:")
main_greedy2(500, data_set_0_25)
print("dynamique:")
main_dynamique(500, data_set_0_25)

""" print("set1")
print("greedy1:")
main_greedy1(500, data_set_1)
print("greedy2:")
main_greedy2(500, data_set_1)
print("dynamique:")
main_dynamique(500, data_set_1)

print("set2")
print("greedy1:")
main_greedy1(500, data_set_2)
print("greedy2:")
main_greedy2(500, data_set_2)
print("dynamique:")
main_dynamique(500, data_set_2)


print("set4")
print("greedy1:")
main_greedy1(500, data_set_4)
print("greedy2:")
main_greedy2(500, data_set_4)
print("dynamique:")
main_dynamique(500, data_set_4)  """