def knapsack(values: list[int], weights: list[int], capacity: int):
    dp = [0] * (capacity + 1) 
    for i in range(len(values)):
        new_dp = dp.copy()
        for j in range(1, capacity + 1):

            if weights[i] <= j:
                new_dp[j] = max(dp[j], values[i] + dp[j - weights[i]])

        dp = new_dp

    return dp[-1]


def solution():
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    capacity = int(input())
    # values = [10, 500, 20]
    # weights = [1, 1, 2]
    # capacity = 4
    print(knapsack(values, weights, capacity))

solution()