# 골드 4

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
board, empty, virus = [], [], []
max_safe = 0

for i in range(n):
    line = input().split()
    board.append(line)
    for j in range(m):
        if line[j] == "0":
            empty.append((i, j))
        elif line[j] == "2":
            virus.append((i, j))

for case in combinations(empty, 3):
    temp = [list(line) for line in board]
    queue = deque(virus)
    safe = len(empty) - 3

    for x, y in case:
        temp[x][y] = "1"

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == "0":
                temp[nx][ny] = "2"
                safe -= 1
                queue.append((nx, ny))

    max_safe = max(safe, max_safe)

print(max_safe)
