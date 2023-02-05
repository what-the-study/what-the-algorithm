# 실버 1

import sys
from collections import deque

input = sys.stdin.readline


def get_target_xy():
    for i in range(n):
        for j in range(m):
            if board[i][j] == "2":
                return i, j


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx == target_x and ny == target_y:
                continue
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "1" and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return


n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

target_x, target_y = get_target_xy()
bfs(target_x, target_y)

for i in range(n):
    for j in range(m):
        if abs(target_x - i) + abs(target_y - j) > 1 and board[i][j] == "1" and distance[i][j] == 0:
            distance[i][j] = -1

for line in distance:
    print(*line)
