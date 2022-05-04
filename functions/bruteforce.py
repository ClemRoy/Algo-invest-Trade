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


def prepare_action_list(action_list):
    for action in action_list: #O(n)
        action["price"] = float(action["price"]) #O(1)
        action["profit"] = float(action["profit"]) #O(1)
        action["returns"] = action["price"]*(action["profit"]/100) #O(1)
    return action_list #O(n)*(O(1)*3)=O(n)


def brute_force(budget, action_list, selected_elelemnts=[]):
    if action_list: #O(1)
        total_returns1, selected_actions1 = brute_force(
            budget, action_list[1:], selected_elelemnts) #O(n) b+=1
        action = action_list[0] #O(1)
        if action["price"] <= budget: #O(1)
            total_returns2, selected_actions2 = brute_force(
                budget-action["price"], action_list[1:], selected_elelemnts+[action]) #O(n) b+=1
            if total_returns1 < total_returns2: #O(1)
                return total_returns2, selected_actions2  #O(1)
        return total_returns1, selected_actions1  #O(1)

    else:
        return sum([action["returns"] for action in selected_elelemnts]), selected_elelemnts  #O(1)
    #O(1)*6+(O(b^n))= O(2^n)


def calculate_cost(comb):
    cost = 0 #O(1)
    for action in comb: #O(n)
        cost += float(action["price"]) #O(1)
    return cost #O(n)*(O(1)*2)= O(n)


def calculate_returns(comb):
    returns = 0 #O(1)
    for action in comb: #O(n)
        returns += action["returns"] #O(1)
    return returns #O(n)*(O(1)*2)=O(n)


def calculate_profit(comb):
    cost = calculate_cost(comb) #O(n)
    returns = calculate_returns(comb) #O(n)
    profit = (returns/cost)*100 #O(1)
    return profit #(O(n)*2)*O(1) = O(2n) = O(n)


def main_bruteforce_hm(action_list):
    start = timer() #O(1)
    prepared_action_list = prepare_action_list(action_list) #O(n)
    _,r = brute_force(500, prepared_action_list)  #O(2^n)
    end = timer() #O(1)
    print(f"durée du script: {end-start}") #O(1)
    print(f"cout de la combinaison: {calculate_cost(r)}") #O(n)
    print(f"retours de la combinaison: {calculate_returns(r)}") #O(n)
    print(f"cout de la combinaison: {calculate_profit(r)}") #O(n)
    print("liste des actions:") #O(1)
    print(r) #O(1)
    #O(2^n)