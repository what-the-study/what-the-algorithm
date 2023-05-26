# 골드 1

import sys

input = sys.stdin.readline
INF = 99999999

n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] for i in range(n)]
dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        prefix[i].append(prefix[i][j] + a[i][j])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        dp[x][y] = min(dp[x - 1][y], prefix[x - 1][n] - prefix[x - 1][y - 1])

for _ in range(q):
    sx, sy, l = map(int, input().split())
    min_period = prefix[sx - 1][n] - prefix[sx - 1][sy - 1]

    for y in range(sy, n + 1):
        period = prefix[sx - 1][y] - prefix[sx - 1][sy - 1] - a[sx - 1][y - 1]
        min_period = min(min_period, period + dp[sx - l][y])

    print(min_period)
