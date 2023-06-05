# 골드 2

import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    queue = deque([node])
    counts = [k + 2] * (n + 2)
    counts[node] = 0

    while queue:
        node = queue.popleft()

        for next_node, fuel in graph[node]:
            if counts[node] + 1 < counts[next_node] and fuel <= capacity:
                counts[next_node] = counts[node] + 1
                queue.append(next_node)

    return bool(counts[n + 1] != k + 2)


n, k = map(int, input().split())
xy = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)] + [[10000, 10000]]
graph = [[] for _ in range(n + 2)]

for i in range(n + 1):
    x1, y1 = xy[i]
    for j in range(i + 1, n + 2):
        x2, y2 = xy[j]
        dist = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
        fuel = dist // 10 if dist == int(dist) else dist // 10 + 1
        graph[i].append((j, fuel))
        graph[j].append((i, fuel))

start, end = 1, 1500
min_capacity = end

while start <= end:
    capacity = (start + end) // 2

    if bfs(0):
        min_capacity = capacity
        end = capacity - 1
    else:
        start = capacity + 1

print(min_capacity)
