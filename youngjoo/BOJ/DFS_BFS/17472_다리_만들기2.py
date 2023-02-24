# 골드 1

import sys
from collections import deque

input = sys.stdin.readline


def set_bridge(board):
    for i in range(len(board)):
        s, w = 0, 0
        for j in range(len(board[0])):
            if s == 0:
                if board[i][j] > 0:
                    s = board[i][j]
            elif board[i][j] == 0:
                w += 1
            elif s == board[i][j]:
                w = 0
            else:
                if w > 1:
                    e = board[i][j]
                    bridges[(s, e)] = min(w, bridges[(s, e)]) if (s, e) in bridges else w
                s = board[i][j]
                w = 0


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # path compression
    return parent[node]


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
island_type = 1

# 1. BFS
for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] == 1:
            visited[i][j] = True
            maps[i][j] = island_type
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        maps[nx][ny] = island_type
                        queue.append((nx, ny))

            island_type += 1

# 2. Set bridges
bridges = {}
set_bridge(maps)
set_bridge(list(zip(*maps)))

# 3. Kruskal
node_counts = island_type - 1
edges = sorted((bridges[(s, e)], s, e) for s, e in bridges)

parent = list(range(node_counts + 1))
counts = 0
cost = 0

for w, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root
        cost += w
        counts += 1

        if counts >= node_counts - 1:
            break

for node in range(1, len(parent)):
    find_set(node)

print(cost if len(set(parent[1:])) == 1 else -1)
