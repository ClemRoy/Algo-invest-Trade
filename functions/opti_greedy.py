import csv
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(10000)

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e

available_action_list = []

with open("E:\L7\dataset2_Python+P7.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        available_action_list.append(row)


def prepare_action_list(action_list):
    filtered_actions = [] #O(1)
    for action in action_list: #O(n)
        if float(action["price"]) > 0 and float(action["profit"]) > 0: #O(1)*4
            action["price"] = float(action["price"]) #O(1)*2
            action["profit"] = float(action["profit"]) #O(1)*2
            action["returns"] = calculate_return(action) #O(1)
            filtered_actions.append(action) #O(1)
    sorted_list = sorted(
        filtered_actions, key=lambda x: float(x["profit"])) #O(n log(n))
    return sorted_list #O(n)


def calculate_return(action):
    returns = action["price"] * (action["profit"]/100) #O(4)
    return returns #O(1)
    #O(1)

def calculate_comb_cost(comb):
    cost = 0  #O(1)
    for action in comb: #O(n)
        cost += action["price"] #O(1)
    return cost #O(1)
    #O(1)*O(n) = O(n)


def calculate_comb_returns(comb):
    returns = 0
    for action in comb:
        returns += action["returns"]
    return returns #O(n)


def calculate_comb_profit(comb):
    cost = calculate_comb_cost(comb) #O(n)
    returns = calculate_comb_returns(comb) #O(n)
    profit = (returns/cost)*100 #O(5)
    return profit #O(n)


def greedy1(budget, action_list):
    selected_actions = [] #O(1)
    total_price = 0 #O(1)
    while action_list: #O(log(n))
        action = action_list.pop() #O(1)
        if action["price"] + total_price <= budget: #O(4)
            selected_actions.append(action) #O(1)
            total_price += action["price"] #O(1)
    return selected_actions #O(log(n))


def greedy_rec(action_list, chosen_action=[], budget=500):
    while action_list: #O( log(n))
        action = action_list.pop() #O(1)
        if action["price"] <= budget: #O(1)
            chosen_action.append(action) #O(1)
            greedy_rec(action_list, chosen_action, budget-action["price"]) #O(n) (pas de branches)
        else:
            greedy_rec(action_list, chosen_action, budget) #O(n) (pas de branches)
    return chosen_action #O(log(n))


def main_greedy1(budget, action_list):
    start = timer() #O(1)
    prepared_action_list = prepare_action_list(action_list) #O(n log(n))
    result = greedy1(budget, prepared_action_list)  #O(log(n))
    end = timer() #O(1)
    print(f"durée du script: {end-start}") #O(1)
    print(f"cout de la combinaison: {calculate_comb_cost(result)}") #O(1)
    print(f"retours de la combinaison: {calculate_comb_returns(result)}") #O(1)
    print(f"profit de la combinaison: {calculate_comb_profit(result)}") #O(1)
    print("liste des actions:") #O(1)
    print(result) #O(1)
    #O(n log(n))


def main_greedy2(budget, action_list):
    start = timer()
    prepared_action_list = prepare_action_list(action_list) #O(n log(n))
    acc = []
    result = greedy_rec(prepared_action_list, acc, budget) #O(log(n))
    end = timer()
    print(f"durée du script: {end-start}")
    print(f"cout de la combinaison: {calculate_comb_cost(result)}")
    print(f"retours de la combinaison: {calculate_comb_returns(result)}")
    print(f"profit de la combinaison: {calculate_comb_profit(result)}")
    print("liste des actions:")
    print(result)
    #O(n log(n))