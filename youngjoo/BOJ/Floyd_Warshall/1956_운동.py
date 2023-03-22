# 골드 4

import sys

input = sys.stdin.readline
INF = 99999999

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]
min_dist = INF

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        if k == i:
            continue
        for j in range(v):
            if i == j or k == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(v):
    for j in range(i + 1, v):
        min_dist = min(min_dist, graph[i][j] + graph[j][i])

print(min_dist if min_dist < INF else -1)
