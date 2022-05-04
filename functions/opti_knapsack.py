import csv
from timeit import default_timer as timer

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e

available_action_list = []

with open("E:\L7\dataset0.csv", "r") as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        available_action_list.append(row)


def calculate_comb_cost(comb):
    cost = 0 #O(1)
    for action in comb: #O(n)
        cost += action["price"] #O(1)
    return cost #O(n)


def calculate_comb_returns(comb):
    returns = 0 #O(1)
    for action in comb: #O(n)
        returns += action["returns"] #O(1)
    return returns #O(n)


def calculate_comb_profit(comb):
    cost = calculate_comb_cost(comb) #O(n)
    returns = calculate_comb_returns(comb) #O(n)
    profit = (returns/cost)*100 #O(1)
    return profit #O(n)


def prepare_action_list(action_list):
    filtered_actions = []
    for action in action_list: #O(n)
        if float(action["price"]) > 0 and float(action["profit"]) > 0: #O(1)
            returns = (float(action["price"])*(float(action["profit"])/100)) #O(1)
            action["price"] = int(float(action["price"])*100) #O(1)
            action["profit"] = int(float(action["profit"])*100) #O(1)
            action["returns"] = returns #O(1)
            filtered_actions.append(action) #O(1)
    sorted_list = sorted(
        filtered_actions, key=lambda x: float(x["profit"]), reverse=True)  #O(n log(n))
    return sorted_list #O(n log(n))


def knapsack_dynamique(raw_budget, raw_action_list): #n= action_list;w=budget
    action_list = prepare_action_list(raw_action_list) #O(n log(n))
    budget = raw_budget*100 #O(1)
    matrice = [[0 for x in range(budget + 1)]
               for x in range(len(action_list)+1)] #O(n*w)
    for i in range(1, len(action_list)+1):  #O(n)
        for w in range(1, budget+1):  #O(w)
            if action_list[i-1]["price"] <= w: #O(1)
                matrice[i][w] = max((action_list[i-1]["returns"])+matrice[i-1]
                                    [w-(action_list[i-1]["price"])], matrice[i-1][w]) #O(n)
            else:
                matrice[i][w] = matrice[i-1][w] #O(1)

    w = budget #O(1)
    n = len(action_list) #O(1)
    selected_actions = [] #O(1)
    while w >= 0 and n >= 0: #O(log(n))
        e = action_list[n-1] #O(1)
        if matrice[n][w] == matrice[n-1][w-e["price"]] + e["returns"]: #O(1)
            selected_actions.append(e) #O(1)
            w -= e["price"] #O(1)
        n -= 1 #O(1)
    return selected_actions
    #O(n*w)

def return_value_to_normal(action_list):
    for action in action_list: #O(n)
        old_price = float(action["price"])/100 #O(1)
        old_profit = float(action["profit"])/100 #O(1)
        action["price"] = old_price #O(1)
        action["profit"] = old_profit #O(1)
    return action_list #O(n)


def main_dynamique(budget, action_list):
    start = timer()  #O(1)
    results = knapsack_dynamique(budget, action_list)   #O(n*w)
    restaured_value_results = return_value_to_normal(results) #O(n)
    end = timer() #O(1)
    print(f"durée du script: {end-start}")  #O(1)
    print(
        f"cout de la combinaison: {calculate_comb_cost(restaured_value_results)}")  #O(1)
    print(
        f"retours de la combinaison: {calculate_comb_returns(restaured_value_results)}")  #O(1)
    print(
        f"profit de la combinaison: {calculate_comb_profit(restaured_value_results)}")  #O(1)
    print("liste des actions:")  #O(1)
    print(restaured_value_results)  #O(1)
     #O(n*w)