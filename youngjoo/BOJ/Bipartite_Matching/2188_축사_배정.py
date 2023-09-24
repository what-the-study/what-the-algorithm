# 플래티넘 4

import sys

input = sys.stdin.readline
NOT_MATCHED = -1


def dfs(cow):
    if visited[cow]:
        return False

    visited[cow] = True

    for barn in graph[cow]:
        if matching[barn] == NOT_MATCHED:
            matching[barn] = cow
            return True

    for barn in graph[cow]:
        if dfs(matching[barn]):
            matching[barn] = cow
            return True

    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
matching = [NOT_MATCHED] * (m + 1)
result = 0

for cow in range(1, n + 1):
    _, *barns = list(map(int, input().split()))
    graph[cow] = barns

for cow in range(1, n + 1):
    visited = [False] * (n + 1)
    result += int(dfs(cow))

    if result == m:
        break

print(result)
