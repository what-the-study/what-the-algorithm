# 플래티넘 4

import sys

input = sys.stdin.readline
NOT_MATCHED = 0


def dfs(employee):
    if visited[employee]:
        return False

    visited[employee] = True

    for work in graph[employee]:
        if matching[work] == NOT_MATCHED:
            matching[work] = employee
            return True

    for work in graph[employee]:
        if dfs(matching[work]):
            matching[work] = employee
            return True

    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = 0

for employee in range(1, n + 1):
    _, *works = list(map(int, input().split()))
    graph[employee] = works

matching = [NOT_MATCHED] * (m + 1)

for employee in range(1, n + 1):
    visited = [False] * (n + 1)
    result += int(dfs(employee))

    visited = [False] * (n + 1)
    result += int(dfs(employee))

    if result == m:
        break

print(result)
