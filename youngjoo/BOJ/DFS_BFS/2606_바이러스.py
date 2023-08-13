# 실버 3

import sys

input = sys.stdin.readline


def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)

print(sum(visited) - 1)
