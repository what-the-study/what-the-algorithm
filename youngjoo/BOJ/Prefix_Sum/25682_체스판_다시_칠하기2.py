# 골드 5

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
min_changes = n * m

black = [[0] * m for _ in range(n)]
white = [[0] * m for _ in range(n)]
p_black = [[0] * (m + 1) for _ in range(n + 1)]
p_white = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if i % 2 == j % 2:
            if board[i][j] == "W":
                black[i][j] = 1
            else:
                white[i][j] = 1
        else:
            if board[i][j] == "B":
                black[i][j] = 1
            else:
                white[i][j] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        p_black[i][j] = p_black[i - 1][j] + p_black[i][j - 1] - p_black[i - 1][j - 1] + black[i - 1][j - 1]
        p_white[i][j] = p_white[i - 1][j] + p_white[i][j - 1] - p_white[i - 1][j - 1] + white[i - 1][j - 1]

for i in range(k, n + 1):
    for j in range(k, m + 1):
        s_black = p_black[i][j] - p_black[i - k][j] - p_black[i][j - k] + p_black[i - k][j - k]
        s_white = p_white[i][j] - p_white[i - k][j] - p_white[i][j - k] + p_white[i - k][j - k]
        min_changes = min(min_changes, s_black, s_white)

print(min_changes)
