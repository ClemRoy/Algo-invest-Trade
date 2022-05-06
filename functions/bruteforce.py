from functions.utils import extract_data
# price = prix en e
# profit = profit exprimé en % du prixm
# return = montant gagné en e


def prepare_action_list(action_list: list):
    """
    Take list of data extracted from csv file,turns relevant strings into
    float and add action returns the return the list
    """
    for action in action_list:  # O(n)
        action["price"] = float(action["price"])  # O(1)
        action["profit"] = float(action["profit"])  # O(1)
        action["returns"] = action["price"]*(action["profit"]/100)  # O(1)
    return action_list  # O(n)*(O(1)*3)=O(n)


def calculate_comb_cost(comb):
    """
    Takes a combination as a list of action and return it's total cost
    """
    cost = 0  # O(1)
    for action in comb:  # O(n)
        cost += action["price"]  # O(1)
    return cost  # O(1)*(O(n)*O(1)) = O(n)


def calculate_comb_returns(comb):
    """
    Takes a combination as a list of action and return it's total returns
    """
    returns = 0  # O(1)
    for action in comb:  # O(n)
        returns += action["returns"]  # O(1)
    return returns  # O(n)*(O(1)*2)=O(n)


def calculate_profit(comb):
    """
    Take a combination as a list of actions,calculate it's total 
    cost and returns and return the global profit"""
    cost = calculate_comb_cost(comb)  # O(n)
    returns = calculate_comb_returns(comb)  # O(n)
    profit = (returns/cost)*100  # O(1)
    return profit  # (O(n)*2)*O(1) = O(2n) = O(n)


def brute_force(budget, action_list, selected_elements=None):
    """Declare a list of empty selected action when first launched,
    if there is an action in the action list:"""
    if selected_elements == None:
        selected_elements = []
    if action_list:  # O(1)
        total_returns1, selected_actions1 = brute_force(
            budget, action_list[1:], selected_elements)  # O(n) b+=1
        action = action_list[0]  # O(1)
        if action["price"] <= budget:  # O(1)
            total_returns2, selected_actions2 = brute_force(
                budget-action["price"], action_list[1:], selected_elements+[action])  # O(n) b+=1
            if total_returns1 < total_returns2:  # O(1)
                return total_returns2, selected_actions2  # O(1)
        return total_returns1, selected_actions1  # O(1)

    else:
        # O(1)
        return sum([action["returns"] for action in selected_elements]), selected_elements
    # O(1)*6+(O(b^n))= O(2^n)


def main_bruteforce_hm(budget: int, data_path: str):
    """take the budget as an int,the path to the csv file as a string,
    and display the best combination cost,returns, its global profit 
    and the actions list"""
    raw_data = extract_data(data_path)
    prepared_action_list = prepare_action_list(raw_data)  # O(n)
    _, r = brute_force(budget, prepared_action_list)  # O(2^n)
    print(f"cout de la combinaison: {calculate_comb_cost(r)}")  # O(n)
    print(f"retours de la combinaison: {calculate_comb_returns(r)}")  # O(n)
    print(f"profits de la combinaison: {calculate_profit(r)}")  # O(n)
    print("liste des actions:")  # O(1)
    print(r)  # O(1)
    # O(2^n)


if __name__ == "__main__":
    main_bruteforce_hm(500, "E:\L7\Livrable\dataset0.csv")
