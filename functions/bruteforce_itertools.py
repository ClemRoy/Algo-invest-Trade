import csv
import itertools
from timeit import default_timer as timer

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e

available_action_list = []

with open("E:\L7\dataset0.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        available_action_list.append(row)


def prepare_list(action_list):
    for action in action_list:  # O(n)
        action["price"] = float(action["price"])  # O(1)
        action["profit"] = float(action["profit"])  # O(1)
        action["returns"] = action["price"]*(action["profit"]/100)  # O(1)
    return action_list  # O(n) * O(1)* = O(n)


def calculate_comb_returns(comb):
    returns = 0  # O(1)
    for action in comb:  # O(n)
        returns += action["returns"]  # O(1)
    return returns  # O(1)*(O(n)*O(n)) = O(n)


def calculate_comb_cost(comb):
    cost = 0  # O(1)
    for action in comb:  # O(n)
        cost += action["price"]  # O(1)
    return cost  # O(1)*(O(n)*O(1)) = O(n)


def calculate_profit(returns, cost):
    profit = (returns/cost)*100  # O(3)
    return profit  # =O(1)


def bruteforce_itertools(budget, action_list):
    prepared_list = prepare_list(action_list)  # O(n)
    combination_count = 0  # O(1)
    best_returns = 0  # O(1)
    best_comb_cost = 0  # O(1)
    comb_with_best_returns = []  # O(1)
    for L in range(0, len(prepared_list)+1):  # O(n)
        for combination in itertools.combinations(prepared_list, L):  # O(n!)
            combination_count += 1  # O(1)
            comb_as_list = list(combination)  # O(1)
            comb_cost = calculate_comb_cost(comb_as_list)  # O(1)
            if comb_cost <= budget:  # O(1)
                comb_returns = calculate_comb_returns(comb_as_list)  # O(1)
                if comb_returns > best_returns:  # O(1)
                    best_returns = comb_returns  # O(1)
                    best_comb_cost = comb_cost  # O(1)
                    comb_with_best_returns = comb_as_list  # O(1)
    # O(n)+(O(1)*4)+(O(n)*O(n)*O(1)*9 = O(n)+O(1)+(O(n²)*O(1)) = O(n!)
    return best_returns, best_comb_cost, comb_with_best_returns


def main_itertools(budget, action_list):
    start = timer()  # O(1)
    returns, cost, comb = bruteforce_itertools(budget, action_list)  # O(n²)
    profit = calculate_profit(returns, cost)  # O(1)
    end = timer()  # O(1)
    print(f"durée du script: {end-start}")  # O(1)
    print(
        f"cout de la combinaison: {cost}")  # O(1)
    print(
        f"retours de la combinaison: {returns}")  # O(1)
    print(
        f"profit de la combinaison: {profit}")  # O(1)
    print("liste des actions:")  # O(1)
    print(comb)  # O(1)
    # O(1)*9+O(n²)= O(n!