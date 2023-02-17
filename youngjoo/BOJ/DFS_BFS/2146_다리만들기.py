# 골드 3

import sys
from collections import deque

input = sys.stdin.readline


# 섬의 경계선인지 확인하는 함수
def is_border(x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == [0, 0]:
            return True
    return False


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
island = 2  # 섬 종류

# 1. 지도를 섬 별로 나누고, 각 좌표를 [섬 종류, 0]으로 초기화하기
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            maps[i][j] = [island, 0]
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                        maps[nx][ny] = [island, 0]  # [섬 종류, 섬에서 부터 떨어진 거리]
                        queue.append((nx, ny))

            island += 1
        elif maps[i][j] == 0:
            maps[i][j] = [0, 0]

starts = deque()  # 동시다발적으로 출발할 섬의 경계 큐
min_length = n * 2

for i in range(n):
    for j in range(n):
        if maps[i][j][0] > 0 and is_border(i, j):
            starts.append((i, j))  # 섬의 경계 좌표 모두 큐에 넣기

# 2. 섬의 경계에서 동시다발적으로 출발하여 서로 다른 두 섬에서 온 경로가 만나면 그 즉시 최소거리 갱신
while starts:
    i, j = starts.popleft()
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < n and 0 <= nj < n and maps[i][j][0] != maps[ni][nj][0]:
            if maps[ni][nj][0] == 0:
                maps[ni][nj][0] = maps[i][j][0]
                maps[ni][nj][1] += maps[i][j][1] + 1
                starts.append((ni, nj))
            else:
                min_length = min(min_length, maps[i][j][1] + maps[ni][nj][1])

print(min_length)
