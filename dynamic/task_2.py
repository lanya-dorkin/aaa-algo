def rob_corovans(values: list):
    
    dp = [0] * len(values)
    dp[0] = values[0]

    if len(values) > 1:
        dp[1] = max(values[:2])

    for i in range(2, len(values)):
        dp[i] = max(dp[i-1], dp[i-2] + values[i])

    return dp[-1]


def solution():
    values = list(map(int, input().split()))
    # values = [1, 7, 1, 3, 14]
    print(rob_corovans(values))


solution()
