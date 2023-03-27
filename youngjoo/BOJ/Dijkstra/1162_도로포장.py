# 골드 1

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e10)


def dijkstra(node):
    # distance[a][b] => b번 포장하여 a 정점까지 갔을 때의 최단 거리
    distance = [[INF] * (k + 1) for _ in range(n + 1)]
    distance[node] = [0] * (k + 1)
    heap = [(0, node, 0)]  # (min_dist, node, pavings)

    while heap:
        min_dist, node, pavings = heappop(heap)

        if min_dist > distance[node][pavings]:
            continue

        for next_node, dist in graph[node]:
            # 1. 포장 하고 이동
            next_dist = distance[node][pavings]
            if pavings < k and next_dist < distance[next_node][pavings + 1]:
                distance[next_node][pavings + 1] = next_dist
                heappush(heap, (next_dist, next_node, pavings + 1))

            # 2. 포장 안하고 이동
            next_dist = distance[node][pavings] + dist
            if next_dist < distance[next_node][pavings]:
                distance[next_node][pavings] = next_dist
                heappush(heap, (next_dist, next_node, pavings))

    return min(distance[n])


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(dijkstra(1))
