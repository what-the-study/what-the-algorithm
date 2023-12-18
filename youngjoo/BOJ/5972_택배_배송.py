# 골드 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            new_dist = min_dist + dist

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

print(distance[n])
