# 실버 3

import sys

input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(2)]

dp[0][1], dp[1][1] = stair[0], stair[0]

for i in range(2, n + 1):
    dp[0][i] = dp[1][i - 1] + stair[i - 1]
    dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + stair[i - 1]

print(max(dp[0][n], dp[1][n]))
