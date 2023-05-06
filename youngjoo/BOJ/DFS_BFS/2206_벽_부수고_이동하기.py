# 골드 3

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y, z):
    dist = [[[0, 0] for _ in range(m)] for _ in range(n)]  # [안부숨, 부숨]
    dist[x][y][z] = 1
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist[x][y][z]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny][z] == 0 and board[nx][ny] == 0:
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    queue.append((nx, ny, z))
                elif z == 0 and board[nx][ny] == 1:
                    dist[nx][ny][1] = dist[x][y][z] + 1
                    queue.append((nx, ny, 1))

    return -1


n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs(0, 0, 0))
