# 실버 1

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
board = [input().split() for _ in range(m)]
result = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == "1":
            board[i][j] = "0"
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "1":
                        board[nx][ny] = "0"
                        queue.append((nx, ny))

            result += 1

print(result)
