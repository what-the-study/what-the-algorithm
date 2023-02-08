# 실버 1

import sys

input = sys.stdin.readline


def dfs(x, y):
    for i in range(2):
        nx, ny = x + dx[i] * board[x][y], y + dy[i] * board[x][y]
        if nx < n and ny < n and not visited[nx][ny]:
            if board[nx][ny] == -1:
                global result
                result = "HaruHaru"
                return
            visited[nx][ny] = True
            dfs(nx, ny)


n = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [1, 0], [0, 1]
result = "Hing"

visited[0][0] = True
dfs(0, 0)

print(result)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def bfs(x, y):
#     visited[x][y] = True
#     queue = deque([(x, y)])
#     while queue:
#         x, y = queue.popleft()
#         for i in range(2):
#             nx, ny = x + dx[i] * board[x][y], y + dy[i] * board[x][y]
#             if nx < n and ny < n and not visited[nx][ny]:
#                 if board[nx][ny] == -1:
#                     return "HaruHaru"
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#
#     return "Hing"
#
#
# n = int(input().rstrip())
# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# dx, dy = [1, 0], [0, 1]
#
# print(bfs(0, 0))
