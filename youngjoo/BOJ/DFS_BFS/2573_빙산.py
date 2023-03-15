# 골드 4

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny] == 0 and sea[nx][ny] > 0:
            visited[nx][ny] = ice_type
            dfs(nx, ny)


n, m = map(int, input().split())
sea = []
iceberg = []

for x in range(n):
    line = list(map(int, input().split()))
    sea.append(line)
    for y in range(1, m - 1):
        if line[y] > 0:
            iceberg.append((x, y))

year = 0

while True:
    ice_type = 0
    visited = [[0] * m for _ in range(n)]
    melts = [[0] * m for _ in range(n)]

    for x, y in iceberg:
        melts[x][y] = sum(sea[x + dx[i]][y + dy[i]] == 0 for i in range(4))
        if visited[x][y] == 0 and sea[x][y] > 0:
            ice_type += 1
            if ice_type > 1:
                break
            visited[x][y] = ice_type
            dfs(x, y)

    if ice_type == 0:
        year = 0
        break

    if ice_type > 1:
        break

    for x, y in iceberg:
        if sea[x][y] > 0:
            sea[x][y] -= melts[x][y]
            if sea[x][y] <= 0:
                sea[x][y] = 0

    year += 1

print(year)
