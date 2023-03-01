# 골드 4

import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = min_dist + dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
max_total = 0
INF = 999999999

for _ in range(r):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

for node in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(node)
    total = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            total += items[i - 1]
    max_total = max(total, max_total)

print(max_total)
