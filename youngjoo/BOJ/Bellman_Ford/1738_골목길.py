# 골드 1

import sys
from collections import deque

input = sys.stdin.readline
INF = 99999999


def can_reach_end(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                if next_node == n:
                    return True
                visited[next_node] = True
                queue.append(next_node)

    return False


def bellman_ford(start):
    distance = [INF] * (n + 1)
    pre_node = [0] * (n + 1)
    distance[start] = 0
    pre_node[start] = 0

    for i in range(n):
        is_updated = False

        for u, v, w in edges:
            next_dist = distance[u] + w
            if distance[u] < INF and next_dist < distance[v]:
                # 사이클이 발생하고, 그 사이클을 통해 도착 정점에 도달할 수 있으면, 최적 경로는 없음
                if i == n - 1 and can_reach_end(v):
                    return "-1"
                is_updated = True
                distance[v] = next_dist
                pre_node[v] = u

        if not is_updated:
            break

    path = []
    end = n

    while end > 0:
        path.append(str(end))
        end = pre_node[end]

    return " ".join(path[::-1])


n, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, -w))
    graph[u].append(v)

print(bellman_ford(1))
