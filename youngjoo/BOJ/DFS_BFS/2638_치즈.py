# 골드 3

import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not outsides[nx][ny] and cheese[nx][ny] == "0":
                outsides[nx][ny] = True
                queue.append((nx, ny))


def is_exposed(x, y):
    counts = 0

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if outsides[nx][ny]:
            counts += 1

    return counts >= 2


n, m = map(int, input().split())
cheese = [input().split() for _ in range(n)]
outsides = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

melts = deque([(0, 0)])
outsides[0][0] = True
hours = 0

while True:
    bfs(melts)
    melts = deque()

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if cheese[i][j] == "1" and is_exposed(i, j):
                melts.append((i, j))

    if not melts:
        break

    for i, j in melts:
        cheese[i][j] = "0"
        outsides[i][j] = True

    hours += 1

print(hours)
