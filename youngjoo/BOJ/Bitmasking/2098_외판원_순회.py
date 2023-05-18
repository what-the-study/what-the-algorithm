# 골드 1

import sys

input = sys.stdin.readline
INF = 99999999


def travel(city, visited):
    if visited == (1 << n) - 1:
        # 1. 모든 정점을 방문하고, 시작 정점으로 돌아갈 수 있는 경우 (해밀턴 순환)
        if w[city][0] > 0:
            return w[city][0]
        # 2. 모든 정점을 방문했으나, 시작 정점으로 돌아갈 수 없는 경우
        return INF

    # 현재 정점을 지났을 때의 최소 비용이 갱신되었다면, dp 값을 그대로 반환
    # 이때 dp값이 INF라면 해당 경로로는 해밀턴 순환을 할 수 없다는 의미
    if dp[city][visited] > 0:
        return dp[city][visited]

    dp[city][visited] = INF  # 최소 비용으로 갱신 해야 하므로 INF로 초기화

    for next_city in range(n):
        if visited & (1 << next_city) == 0 and w[city][next_city] > 0:
            next_cost = travel(next_city, visited | (1 << next_city)) + w[city][next_city]
            dp[city][visited] = min(dp[city][visited], next_cost)

    return dp[city][visited]


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]  # dp[현재정점][방문처리] = 최소비용

print(travel(0, 1))
