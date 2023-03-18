# 플래티넘 5

import sys
from collections import deque

input = sys.stdin.readline
INF = 99999999


def can_reach_end(node):
    visited = [False] * n
    visited[node] = True
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return False


def bellman_ford(node):
    distance = [INF] * n
    distance[node] = -revenue[node]

    for i in range(n):
        is_updated = False

        for s, e, w in edges:
            next_dist = distance[s] + w - revenue[e]
            if distance[s] < INF and next_dist < distance[e]:
                if i == n - 1 and can_reach_end(e):
                    return "Gee"
                is_updated = True
                distance[e] = next_dist

        if not is_updated:
            break

    return -distance[end] if distance[end] < INF else "gg"


n, start, end, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
    graph[s].append(e)

revenue = list(map(int, input().split()))

print(bellman_ford(start))
