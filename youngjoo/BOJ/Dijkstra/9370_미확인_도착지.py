# 골드 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def dijkstra(start):
    distance = [INF] * (n + 1)
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

    return distance


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ends = [int(input()) for _ in range(t)]
    result = []

    s_d = dijkstra(s)
    g_d = dijkstra(g)
    h_d = dijkstra(h)

    for end in ends:
        if s_d[g] + g_d[h] + h_d[end] == s_d[end] or s_d[h] + h_d[g] + g_d[end] == s_d[end]:
            result.append(end)

    print(*sorted(result))
