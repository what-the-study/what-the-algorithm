# 골드 2

import sys

input = sys.stdin.readline


def dfs(node, total):
    global max_node, max_distance

    for next_node, distance in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            new_distance = total + distance
            if new_distance > max_distance:
                max_distance = new_distance
                max_node = next_node
            dfs(next_node, new_distance)


v = int(input().rstrip())
tree = [[] for _ in range(v + 1)]
max_node, max_distance = 1, 0

for _ in range(v):
    s, *edges = map(int, input().split())
    for i in range(0, len(edges) - 1, 2):
        tree[s].append((edges[i], edges[i + 1]))

for _ in range(2):
    visited = [False] * (v + 1)
    visited[max_node] = True
    dfs(max_node, 0)

print(max_distance)
