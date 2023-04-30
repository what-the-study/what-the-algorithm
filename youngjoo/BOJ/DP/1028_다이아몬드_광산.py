# 플래티넘 5

import sys

input = sys.stdin.readline

r, c = map(int, input().split())
mine = [list(map(int, input().rstrip())) for _ in range(r)]
left_down = [[0] * (c + 2) for _ in range(r + 2)]
right_down = [[0] * (c + 2) for _ in range(r + 2)]
max_size = 0

for i in range(r, 0, -1):
    for j in range(c, 0, -1):
        if mine[i - 1][j - 1] == 1:
            left_down[i][j] = left_down[i + 1][j - 1] + 1
            right_down[i][j] = right_down[i + 1][j + 1] + 1

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if mine[i - 1][j - 1] == 1:
            for k in range(min(left_down[i][j], right_down[i][j])):
                size = k + 1
                if left_down[i + k][j + k] >= size and right_down[i + k][j - k] >= size:
                    max_size = max(size, max_size)

print(max_size)
