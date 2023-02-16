# 골드 5

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    distance = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == "L" and visited[nx][ny] == 0:
                distance = visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return distance


# 위아래 혹은 양쪽에 육지가 있는 육지면 어차피 가장 멀 수가 없음 (가지치기)
def is_promising(x, y):
    if 0 < x < n - 1 and maps[x - 1][y] == maps[x + 1][y] == "L":
        return False
    if 0 < y < m - 1 and maps[x][y - 1] == maps[x][y + 1] == "L":
        return False
    return True


n, m = map(int, input().split())
maps = [input().rstrip() for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_distance = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L" and is_promising(i, j):
            max_distance = max(bfs(i, j), max_distance)

print(max_distance)
