import itertools
from functions.utils import extract_data

# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


def prepare_list(action_list: list):
    """
    Take list of data extracted from csv file,turns relevant strings into
    float and add action returns the return the list
    """
    for action in action_list:  # O(n)
        action["price"] = float(action["price"])  # O(1)
        action["profit"] = float(action["profit"])  # O(1)
        action["returns"] = action["price"]*(action["profit"]/100)  # O(1)
    return action_list  # O(n) * O(1)* = O(n)


def calculate_comb_returns(comb:list):
    """
    Takes a list of action and returns the total of all actions returns
    """
    returns = 0  # O(1)
    for action in comb:  # O(n)
        returns += action["returns"]  # O(1)
    return returns  # O(1)*(O(n)*O(n)) = O(n)


def calculate_comb_cost(comb):
    """
    Takes a list of action and return it's total cost
    """
    cost = 0  # O(1)
    for action in comb:  # O(n)
        cost += action["price"]  # O(1)
    return cost  # O(1)*(O(n)*O(1)) = O(n)


def calculate_profit(returns:float, cost:float):
    """
    Takes returns and cost of action and return it's profit
    """
    profit = (returns/cost)*100  # O(3)
    return profit  # =O(1)


def bruteforce_itertools(budget, action_list):
    """takes data extracted from csv,turns the data into relevant 
    type and add actions returns.Declare an empty list for the
    best action combination, and variables at 0 for the combination 
    cost and returns.
    Goes through each possible combination, if the current combination 
    cost is under the budget,and the returns are betters,the combination 
    is saved as the new best combination.
    Return the saved combination as a tuple of the best combination 
    returns(float),cost(float) and action list
    """
    prepared_list = prepare_list(action_list)  # O(n)
    combination_count = 0  # O(1)
    best_returns = 0  # O(1)
    best_comb_cost = 0  # O(1)
    comb_with_best_returns = []  # O(1)
    for combination_size in range(0, len(prepared_list)+1):  # O(n)
        for combination in itertools.combinations(prepared_list, combination_size):  # O(n!)
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


def main_itertools(budget:int, file_path:str):
    """Take maximum budget as int and the path to the csv file as a string
    display the best possible combination,it's cost,returns and profits and
    the list of actions"""
    raw_list = extract_data(file_path)
    returns, cost, comb = bruteforce_itertools(budget, raw_list)  # O(n²)
    profit = calculate_profit(returns, cost)  # O(1)
    print(
        f"cout de la combinaison: {cost}")  # O(1)
    print(
        f"retours de la combinaison: {returns}")  # O(1)
    print(
        f"profit de la combinaison: {profit}")  # O(1)
    print("liste des actions:")  # O(1)
    print(comb)  # O(1)
    # O(1)*9+O(n²)= O(n!

if __name__ == "__main__":
    main_itertools(500,"E:\L7\Livrable\dataset0.csv")