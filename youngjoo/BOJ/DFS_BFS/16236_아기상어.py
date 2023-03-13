# 골드 3

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]  # 상/좌/우/하


def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    heap = [(0, x, y)]

    while heap:
        distance, x, y = heappop(heap)

        if 0 < ocean[x][y] < baby_size:
            return [distance, x, y]

        distance += 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and ocean[nx][ny] <= baby_size:
                visited[nx][ny] = True
                heappush(heap, (distance, nx, ny))

    return []


n = int(input())
ocean = []
baby_x, baby_y = -1, -1
baby_eats = 0
baby_size = 2
total_seconds = 0

for i in range(n):
    line = list(map(int, input().split()))
    ocean.append(line)
    if baby_x == baby_y == -1:
        for j in range(n):
            if line[j] == 9:
                baby_x, baby_y = i, j
                ocean[i][j] = 0
                break

while True:
    fish = bfs(baby_x, baby_y)

    if not fish:
        break

    seconds, baby_x, baby_y = fish
    ocean[baby_x][baby_y] = 0
    total_seconds += seconds
    baby_eats += 1

    if baby_eats == baby_size:
        baby_size += 1
        baby_eats = 0

print(total_seconds)
