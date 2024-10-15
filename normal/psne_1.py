from itertools import product

def main():
    # Input number of players
    num_players = int(input("Enter the number of players: "))

    # Input number of strategies for each player
    strategies = []
    for i in range(num_players):
        num_strategies = int(input(f"Enter the number of strategies for Player {i + 1}: "))
        strategies.append(num_strategies)

    # Initialize payoffs dictionary
    payoffs = {}

    # Input payoffs for each combination of players and their strategies
    for i in range(strategies[0]):  # Loop through strategies of Player 1
        for j in range(strategies[1]):  # Loop through strategies of Player 2
            key = f"({i + 1}, {j + 1})"  # Creating the key for payoffs
            values = input(f"Enter payoffs for {key} (format: player1_payoff player2_payoff): ")
            payoffs[key] = tuple(map(float, values.split()))

    # Display the payoffs
    print("\nPayoffs:")
    for key, value in payoffs.items():
        print(f"Payoff for {key}: Player 1 = {value[0]}, Player 2 = {value[1]}")

    # Iterate over all possible strategies
    all_strategy_profiles = list(product(*[range(1, num + 1) for num in strategies]))

    # Finding Nash equilibria
    nash_equilibria = find_nash_equilibria(payoffs, all_strategy_profiles, strategies)

    # Display Nash equilibria
    print("\nNash Equilibria:")
    for equilibrium in nash_equilibria:
        print(f"Strategy Profile: {equilibrium}")

def best_response(payoffs, current_strategies, strategies):
    best_responses = []

    # Loop through each player to calculate best responses
    for player in range(len(current_strategies)):
        max_payoff = float('-inf')
        best_strategy = None

        # Evaluate each strategy for the current player
        for strategy in range(1, strategies[player] + 1):
            # Create a list of current strategies (convert tuple to list for modification)
            other_strategies = list(current_strategies)
            other_strategies[player] = strategy  # Set the current player's strategy to the new one
            key = f"({', '.join(map(str, other_strategies))})"  # Create the key for payoffs
            
            payoff = payoffs.get(key)

            if payoff:
                player_payoff = payoff[player]
                # Check if this strategy provides a higher payoff
                if player_payoff > max_payoff:
                    max_payoff = player_payoff
                    best_strategy = strategy

        best_responses.append(best_strategy)

    return best_responses

def check_mutual_best_response(best_responses, current_strategies):
    """
    Check if the current strategies of the players are in each other's best responses.
    :param best_responses: List of best response strategies for each player
    :param current_strategies: List of current strategies for each player
    :return: Boolean indicating if there are mutual best responses
    """
    mutual_response = True
    for player in range(len(best_responses)):
        # Check if the current strategy of player is the best response of the other player
        if current_strategies[player] != best_responses[player]:
            mutual_response = False
            break
    return mutual_response

def find_nash_equilibria(payoffs, all_strategy_profiles, strategies):
    nash_equilibria = []

    for current_strategies in all_strategy_profiles:
        # Calculate best response strategies
        best_responses = best_response(payoffs, current_strategies, strategies)

        # Check for mutual best responses
        if check_mutual_best_response(best_responses, current_strategies):
            nash_equilibria.append(current_strategies)

    return nash_equilibria

if __name__ == "__main__":
    main()
