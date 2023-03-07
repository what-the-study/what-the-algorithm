# 플래티넘 5

import sys
from collections import deque

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def bfs(node):
    visited = [0] * (n + 1)
    visited[node] = 0
    queue = deque([node])

    while queue:
        node = queue.popleft()
        for next_node, cost in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = max(visited[node], cost)
                if next_node == y:
                    return visited[next_node]
                queue.append(next_node)


n, m = map(int, input().split())
parent = list(range(n + 1))
counts, total_cost = 0, 0
graph = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

# kruskal
for c, a, b in edges:
    a_root, b_root = find(a), find(b)
    if a_root != b_root:
        graph[a].append((b, c))
        graph[b].append((a, c))
        parent[b_root] = a_root
        total_cost += c
        counts += 1
        if counts >= n - 1:
            break

# bfs
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(total_cost - bfs(x))
