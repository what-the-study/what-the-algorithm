# 골드 3

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def dijkstra(node):
    distance[node] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = dist + distance[node]
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                pre_node[next_node] = node
                heappush(heap, (next_dist, next_node))


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
pre_node = [0] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start)

path = []
temp = end

while temp > 0:
    path.append(temp)
    temp = pre_node[temp]

print(distance[end])
print(len(path))
print(*path[::-1])
