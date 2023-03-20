# 골드 4

import sys

input = sys.stdin.readline
INF = 99999999

n, m = int(input()), int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)

# Floyd Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if k == i:
            continue
        for j in range(1, n + 1):
            if i == j or k == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for line in graph[1:]:
    for dist in line[1:]:
        print(dist if dist < INF else 0, end=" ")
    print()
