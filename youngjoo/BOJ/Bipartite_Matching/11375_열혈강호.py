# 플래티넘 4

import sys

input = sys.stdin.readline
NOT_MATCHED = 0


# 증가 경로 판단 dfs
def dfs(employee):
    if visited[employee]:
        return False

    visited[employee] = True

    # 1. 아직 매칭되지 않은 일이 있다면, 먼저 매칭
    for work in graph[employee]:
        if matching[work] == NOT_MATCHED:
            matching[work] = employee
            return True

    # 2. 인접한 일들이 모두 매칭됐다면, 다른 직원에게 매칭 가능한지 판단
    for work in graph[employee]:
        if dfs(matching[work]):
            matching[work] = employee
            return True

    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
matching = [NOT_MATCHED] * (m + 1)
result = 0

for employee in range(1, n + 1):
    _, *works = list(map(int, input().split()))
    graph[employee] = works

for employee in range(1, n + 1):
    visited = [False] * (n + 1)
    result += int(dfs(employee))

print(result)
