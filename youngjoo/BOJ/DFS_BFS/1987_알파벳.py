# 골드 4

import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def get_index(char):
    return ord(char) - 65


def dfs(x, y, depth):
    global max_moves

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            n_index = get_index(board[nx][ny])
            if visited[n_index]:
                continue
            visited[n_index] = True
            dfs(nx, ny, depth + 1)
            visited[n_index] = False

    max_moves = max(depth, max_moves)


# def bfs(x, y):
#     global max_moves
#     queue = {(x, y, board[x][y])}
#
#     while queue:
#         x, y, path = queue.pop()
#         max_moves = max(len(path), max_moves)
#         if max_moves >= 26:
#             return
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in path:
#                 queue.add((nx, ny, path + board[nx][ny]))


r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
visited = [False] * 26
max_moves = 0

visited[get_index(board[0][0])] = True
dfs(0, 0, 1)
# bfs(0, 0)

print(max_moves)
