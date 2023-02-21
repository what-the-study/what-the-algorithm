# 골드 4

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, k, r = map(int, input().split())
field = [[[0, []] for _ in range(n)] for _ in range(n)]  # [소 종류, [길의 좌표들]]
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

# 길 정보 표시
for _ in range(r):
    x1, y1, x2, y2 = map(int, input().split())
    field[x1 - 1][y1 - 1][1].append((x2 - x1, y2 - y1))
    field[x2 - 1][y2 - 1][1].append((x1 - x2, y1 - y2))

# 소 정보 표시
for _ in range(k):
    x, y = map(int, input().split())
    field[x - 1][y - 1][0] = 1

cow_type = 1  # 서로 만날 수 있는 소 끼리의 종류(영역 표시)
cow_counts = []  # 영역에 따른 각 소의 수 (나중에 쌍을 구할 때 사용)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and field[i][j][0] != 0:
            visited[i][j] = True
            field[i][j][0] = cow_type
            cow_count = 1
            queue = deque([(i, j)])

            while queue:
                x, y = queue.popleft()
                visited[x][y] = True
                for k in range(4):
                    if (dx[k], dy[k]) in field[x][y][1]:
                        continue  # 길이 있으면 건너지 않음
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        if field[nx][ny][0] == 1:  # 방문한 곳이 소이면 영역 표시 및 수+1
                            field[nx][ny][0] = cow_type
                            cow_count += 1

            cow_type += 1
            cow_counts.append(cow_count)

print(sum(c1 * c2 for c1, c2 in combinations(cow_counts, 2)))
