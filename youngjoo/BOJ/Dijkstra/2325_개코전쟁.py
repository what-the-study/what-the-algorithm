# 플래티넘 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def get_min_path(start):
    distances[start] = 0
    heap = [[0, start, [start]]]

    while heap:
        min_dist, node, path = heappop(heap)

        if min_dist > distances[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = min_dist + dist
            if next_dist < distances[next_node]:
                if next_node == n:
                    min_path = path + [next_node]
                distances[next_node] = next_dist
                heappush(heap, [next_dist, next_node, path + [next_node]])

    return min_path


def dijkstra(start):
    global min_path
    distances[start] = 0
    heap = [[0, start]]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distances[node]:
            continue

        for next_node, dist in graph[node]:
            if (node, next_node) == (s, e) or (node, next_node) == (e, s):
                continue
            next_dist = min_dist + dist
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heappush(heap, [next_dist, next_node])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

distances = [INF] * (n + 1)
min_path = get_min_path(1)
max_distance = distances[n]

for i in range(len(min_path) - 1):
    s, e = min_path[i], min_path[i + 1]
    distances = [INF] * (n + 1)
    dijkstra(1)
    max_distance = max(distances[n], max_distance)

print(max_distance)
