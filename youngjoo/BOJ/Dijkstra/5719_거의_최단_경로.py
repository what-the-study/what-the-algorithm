# 플래티넘 5

import sys
from heapq import heappop, heappush
from collections import deque

input = sys.stdin.readline
INF = 99999999


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            if next_node in path[node]:
                continue
            next_dist = min_dist + dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for prev_node, dist in reversed_graph[node]:
            if distance[prev_node] + dist == distance[node]:
                if node not in path[prev_node]:
                    path[prev_node].append(node)
                    queue.append(prev_node)


while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]
    reversed_graph = [[] for _ in range(n)]
    path = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        reversed_graph[v].append((u, p))

    distance = [INF] * n
    dijkstra(s)

    bfs(d)

    distance = [INF] * n
    dijkstra(s)

    print(distance[d] if distance[d] < INF else -1)
