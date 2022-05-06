from functions.utils import extract_data

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


def prepare_action_list(action_list: list):
    """Take the csv data as a list,create an empty list to store filtered data.
    Goes through the csv data, if the action price and profits are above 0,
    the action price and profit are converted to floats and the action return is added
    before adding the action to the filtered action list.
    Sort the filtered action list from worst[0] to best[-1] then returns it.
    """
    filtered_actions = []  # O(1)
    for action in action_list:  # O(n)
        if float(action["price"]) > 0 and float(action["profit"]) > 0:  # O(1)*4
            action["price"] = float(action["price"])  # O(1)*2
            action["profit"] = float(action["profit"])  # O(1)*2
            action["returns"] = calculate_return(action)  # O(1)
            filtered_actions.append(action)  # O(1)
    sorted_list = sorted(
        filtered_actions, key=lambda x: float(x["profit"]))  # O(n log(n))
    return sorted_list  # O(n)


def calculate_return(action: dict):
    """Take an action dictionnary and return the action returns"""
    returns = action["price"] * (action["profit"]/100)  # O(4)
    return returns  # O(1)
    # O(1)


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


def greedy1(budget: int, action_list: list):
    """Take a budget,and a list of action from least[0] profitable 
    to most[-1] profitable.Goes through the action list from the last index
    if the action price is under the available budget,it is added to 
    the selected action list.
    Return the selected actions list when it went through the action list"""
    selected_actions = []  # O(1)
    total_price = 0  # O(1)
    while action_list:  # O(log(n))
        action = action_list.pop()  # O(1)
        if action["price"] + total_price <= budget:  # O(4)
            selected_actions.append(action)  # O(1)
            total_price += action["price"]  # O(1)
    return selected_actions  # O(log(n))


def greedy_rec(budget: int, action_list: list, chosen_action: list = None):
    """Take a budget,and a list of action from least[0] profitable 
    to most[-1] profitable.Goes through the action list from the last index
    if the action price is under the available budget,it is added to 
    the selected action list.
    Return the selected actions list when it went through the action list"""
    if chosen_action == None:
        chosen_action = []
    while action_list:  # O( log(n))
        action = action_list.pop()  # O(1)
        if action["price"] <= budget:  # O(1)
            chosen_action.append(action)  # O(1)
            # O(n) (pas de branches)
            greedy_rec(budget - action["price"], action_list, chosen_action)
        else:
            # O(n) (pas de branches)
            greedy_rec(budget, action_list, chosen_action)
    return chosen_action  # O(log(n))

def main_greedy1(budget: int, data_path: str):
    """take the budget as an int,the path to the csv file as a string,
    and display the best combination cost,returns, its global profit 
    and the actions list"""
    raw_data = extract_data(data_path)
    prepared_action_list = prepare_action_list(raw_data)  # O(n log(n))
    result = greedy1(budget, prepared_action_list)  # O(log(n))
    print(f"cout de la combinaison: {calculate_comb_cost(result)}")  # O(1)
    # O(1)
    print(f"retours de la combinaison: {calculate_comb_returns(result)}")
    print(f"profit de la combinaison: {calculate_comb_profit(result)}")  # O(1)
    print("liste des actions:")  # O(1)
    print(result)  # O(1)
    # O(n log(n))


def main_greedy2(budget: int, data_path: str):
    """take the budget as an int,the path to the csv file as a string,
    and display the best combination cost,returns, its global profit 
    and the actions list"""
    raw_data = extract_data(data_path)
    prepared_action_list = prepare_action_list(raw_data)  # O(n log(n))
    result = greedy_rec(budget, prepared_action_list)  # O(log(n))
    print(f"cout de la combinaison: {calculate_comb_cost(result)}")
    print(f"retours de la combinaison: {calculate_comb_returns(result)}")
    print(f"profit de la combinaison: {calculate_comb_profit(result)}")
    print("liste des actions:")
    print(result)
    # O(n log(n))


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    main_greedy1(500, "E:\L7\Livrable\dataset1_Python+P7.csv")
    main_greedy2(500, "E:\L7\Livrable\dataset1_Python+P7.csv")
