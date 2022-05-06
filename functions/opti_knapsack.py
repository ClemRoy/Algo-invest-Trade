from functions.utils import extract_data

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


def calculate_comb_cost(comb: list):
    """Take a combination as a list of action and return it's total cost"""
    cost = 0  # O(1)
    for action in comb:  # O(n)
        cost += action["price"]  # O(1)
    return cost  # O(1)
    # O(1)*O(n) = O(n)


def calculate_comb_returns(comb: list):
    """Take a combination as a list of action and return it's total returns"""
    returns = 0
    for action in comb:
        returns += action["returns"]
    return returns  # O(n)


def calculate_comb_profit(comb: list):
    """Take a combination as a list of action and return it's global profit"""
    cost = calculate_comb_cost(comb)  # O(n)
    returns = calculate_comb_returns(comb)  # O(n)
    profit = (returns/cost)*100  # O(5)
    return profit  # O(n)


def prepare_action_list(action_list: list):
    """Take the csv data as a list,create an empty list to store filtered data.
    Goes through the csv data, if the action price and profits are above 0,
    the action price and profit are multiplied by 100 and converted into integers,
    the action returns are added to the action dictionary and the dictionary is
    added to the filtered action list
    Sort the filtered action list from worst[0] to best[-1] then returns it.
    """
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


def knapsack_dynamique(raw_budget:int, action_list): #n= action_list;w=budget
    """create a matrice storing the best otpimal solution for each item and weigh available
    to obtain the best optimal combination,then goes back through the matrice to 
    return the best combination of action possible as a list."""
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
    """returns int multiplied by a 100 to their original float value"""
    for action in action_list: #O(n)
        old_price = float(action["price"])/100 #O(1)
        old_profit = float(action["profit"])/100 #O(1)
        action["price"] = old_price #O(1)
        action["profit"] = old_profit #O(1)
    return action_list #O(n)


def main_dynamique(budget: int, data_path: str):
    """take the budget as an int,the path to the csv file as a string,
    and display the best combination cost,returns, its global profit 
    and the actions list"""
    raw_data = extract_data(data_path)
    action_list = prepare_action_list(raw_data) #O(n log(n))
    results = knapsack_dynamique(budget, action_list)   #O(n*w)
    restaured_value_results = return_value_to_normal(results) #O(n)
    print(
        f"cout de la combinaison: {calculate_comb_cost(restaured_value_results)}")  #O(1)
    print(
        f"retours de la combinaison: {calculate_comb_returns(restaured_value_results)}")  #O(1)
    print(
        f"profit de la combinaison: {calculate_comb_profit(restaured_value_results)}")  #O(1)
    print("liste des actions:")  #O(1)
    print(restaured_value_results)  #O(1)
     #O(n*w)

if __name__ == "__main__":
    main_dynamique(500,"E:\L7\Livrable\dataset0.csv")