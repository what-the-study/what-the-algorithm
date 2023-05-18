# 실버 2

import sys

input = sys.stdin.readline


def travel(city, depth, cost):
    global min_cost

    if min_cost <= cost:
        return

    if depth == n - 1 and w[city][0] > 0:
        min_cost = min(cost + w[city][0], min_cost)
        return

    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:
            visited[next_city] = True
            travel(next_city, depth + 1, cost + w[city][next_city])
            visited[next_city] = False


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = 99999999

visited[0] = True
travel(0, 0, 0)

print(min_cost)
