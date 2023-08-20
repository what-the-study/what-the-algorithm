# 골드 5

import sys

input = sys.stdin.readline


def dfs(node):
    if visited[node]:
        if node in path:
            result.extend(path[path.index(node):])
        return

    visited[node] = True
    path.append(node)
    dfs(graph[node])


n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n + 1)
result = []

for i in range(1, n + 1):
    path = []
    dfs(i)

result.sort()
print(len(result), *result, sep="\n")
