# 골드 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def dijkstra(node):
    distance = [INF] * (n + 1)
    distance[node] = 0
    heap = [(0, node)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, cost in graph[node]:
            next_dist = distance[node] + cost
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))

    return distance[end]


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

print(dijkstra(start))
