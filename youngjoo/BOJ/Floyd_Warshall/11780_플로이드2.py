# 골드 2

import sys

input = sys.stdin.readline
INF = 99999999

n, m = int(input()), int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
paths = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    if w < graph[s][e]:
        graph[s][e] = w
        paths[s][e] = [s, e]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if k == i:
            continue
        for j in range(1, n + 1):
            if i == j or k == j:
                continue
            next_dist = graph[i][k] + graph[k][j]
            if next_dist < graph[i][j]:
                graph[i][j] = next_dist
                paths[i][j] = paths[i][k] + paths[k][j][1:]

for line in graph[1:]:
    for dist in line[1:]:
        print(dist if dist < INF else 0, end=" ")
    print()

for line in paths[1:]:
    for path in line[1:]:
        if path == 0:
            print(0)
        else:
            print(len(path), *path)
