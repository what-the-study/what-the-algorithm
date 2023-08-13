# 실버 1

import sys

input = sys.stdin.readline


def dfs(x, y):
    global house
    house += 1
    board[x][y] = 0

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
            dfs(nx, ny)


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            house = 0
            dfs(i, j)
            result.append(house)

print(len(result))
print(*sorted(result), sep="\n")
