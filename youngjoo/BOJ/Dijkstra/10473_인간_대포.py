# 골드 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def dijkstra(node):
    distances = [INF] * (n + 2)
    distances[node] = 0
    heap = [(0, node)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distances[node]:
            continue

        for next_node, w in graph[node]:
            next_dist = distances[node] + w
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heappush(heap, (next_dist, next_node))

    return distances[n + 1]


start = tuple(map(float, input().split()))
end = tuple(map(float, input().split()))
n = int(input())
cannon = [start] + [tuple(map(float, input().split())) for _ in range(n)] + [end]
graph = [[] for _ in range(n + 2)]

for i in range(n + 2):
    sx, sy = cannon[i]
    for j in range(i + 1, n + 2):
        ex, ey = cannon[j]
        distance = ((sx - ex) ** 2 + (sy - ey) ** 2) ** 0.5
        if i == 0 or i == n + 1:
            w = distance / 5  # running
        else:
            w = min(distance / 5, abs(distance - 50) / 5 + 2)  # min(running, riding)
        graph[i].append((j, w))
        graph[j].append((i, w))

print(dijkstra(0))
