# 실버 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def recursion(i, j):
    if dp[i][j] == 0:
        dp[i][j] = cost[i][j] + min(recursion(i + 1, k) for k in range(3) if j != k)

    return dp[i][j]


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[-1] = cost[-1]

print(min(recursion(0, k) for k in range(3)))
