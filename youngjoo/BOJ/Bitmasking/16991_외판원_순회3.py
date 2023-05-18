# 골드 1

import sys

input = sys.stdin.readline
INF = 99999999


def travel(city, visited):
    if visited == (1 << n) - 1:
        return w[city][0]

    if dp[city][visited] > 0:
        return dp[city][visited]

    dp[city][visited] = INF

    for next_city in range(n):
        if visited & (1 << next_city) == 0 and w[city][next_city] > 0:
            next_cost = travel(next_city, visited | (1 << next_city)) + w[city][next_city]
            dp[city][visited] = min(dp[city][visited], next_cost)

    return dp[city][visited]


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]
w = [[0] * n for _ in range(n)]

for i in range(n - 1):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        w[i][j] = w[j][i] = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

print(travel(0, 1))
