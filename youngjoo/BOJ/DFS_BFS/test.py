# 골드 4

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    visited[x][y] = ice_type
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if visited[nx][ny] == 0 and sea[nx][ny] > 0:
                visited[nx][ny] = ice_type
                queue.append((nx, ny))


n, m = map(int, input().split())
sea, icebergs = [], []
ice_type = 0
year = 0

for x in range(n):
    line = list(map(int, input().split()))
    sea.append(line)
    for y in range(1, m - 1):
        if line[y] > 0:
            icebergs.append([x, y, line[y]])

while ice_type < 2:
    # 1. 빙산 녹이기
    for iceberg in icebergs:
        x, y, height = iceberg
        melting = 0

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if sea[nx][ny] == 0:
                melting += 1

        iceberg[2] = 0 if height < melting else height - melting

    # 2. 녹은 빙산 정보로 바다 갱신
    for x, y, height in icebergs:
        sea[x][y] = height

    # 3. 남은 빙산 구하기
    icebergs = [[x, y, height] for x, y, height in icebergs if height > 0]

    # 모든 빙산이 녹으면 break
    if not icebergs:
        year = 0
        break

    # 4. BFS를 통해 빙산 덩어리 구하기
    visited = [[0] * m for _ in range(n)]
    ice_type = 0

    for x, y, _ in icebergs:
        if visited[x][y] == 0:
            ice_type += 1
            if ice_type > 1:
                break
            bfs(x, y)

    year += 1

print(year)
