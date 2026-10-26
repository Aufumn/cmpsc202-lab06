import time


# Phase 1: Naive Recursive Approach
def coin_change_recursive(coins, amount):
    # Base case: no coins are needed to make amount 0
    if amount == 0:
        return 0

    # Start with a number larger than any possible answer
    minimum = float('inf')

    # Try using each coin
    for coin in coins:
        if coin <= amount:
            result = coin_change_recursive(coins, amount - coin)

            # Only consider solutions that can make exact change
            if result != float('inf'):
                minimum = min(minimum, result + 1)

    return minimum


# Phase 2: Top-Down DP (Memoization)
def coin_change_memoized(coins, amount, memo=None):
    # Create a dictionary if one was not provided
    if memo is None:
        memo = {0: 0}

    # Base case
    if amount == 0:
        return 0

    # Return the answer if it has already been calculated
    if amount in memo:
        return memo[amount]

    minimum = float('inf')

    # Try using each coin
    for coin in coins:
        if coin <= amount:
            result = coin_change_memoized(coins, amount - coin, memo)

            if result != float('inf'):
                minimum = min(minimum, result + 1)

    # Save the answer for future calls
    memo[amount] = minimum

    return minimum


# Phase 3: Bottom-Up DP (Tabulation)
def coin_change_dp(coins, amount):
    # dp[i] stores the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case: zero coins are needed for amount 0
    dp[0] = 0

    # Calculate the answer for every amount from 1 to amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Phase 4: Empirical Comparison
if __name__ == "__main__":
    coins = [1, 2, 5]
    amounts = [5, 10, 15, 20, 25, 30]

    print("Coin Change Performance Comparison")
    print("Coins:", coins)
    print()
    print(f"{'Amount':<10}{'Recursive (s)':<18}"
          f"{'Memoized (s)':<18}{'Bottom-Up (s)':<18}")

    for amount in amounts:
        # Time the naive recursive approach
        start = time.perf_counter()
        recursive_result = coin_change_recursive(coins, amount)
        recursive_time = time.perf_counter() - start

        # Time the memoized approach
        start = time.perf_counter()
        memoized_result = coin_change_memoized(coins, amount)
        memoized_time = time.perf_counter() - start

        # Time the bottom-up approach
        start = time.perf_counter()
        dp_result = coin_change_dp(coins, amount)
        dp_time = time.perf_counter() - start

        # Check that all three approaches agree
        assert recursive_result == memoized_result == dp_result

        print(f"{amount:<10}{recursive_time:<18.8f}"
              f"{memoized_time:<18.8f}{dp_time:<18.8f}")
