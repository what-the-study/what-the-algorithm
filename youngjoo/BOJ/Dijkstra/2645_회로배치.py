# 플래티넘 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra(x, y):
    distance = [[INF] * n for _ in range(n)]
    distance[x][y] = 1
    heap = [(1, (x, y), [(x, y)])]

    while heap:
        min_dist, node, path = heappop(heap)
        x, y = node

        if min_dist > distance[x][y]:
            continue

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                next_dist = min_dist + board[nx][ny]
                next_path = path + [(nx, ny)]
                if next_dist < distance[nx][ny]:
                    distance[nx][ny] = next_dist
                    heappush(heap, (next_dist, (nx, ny), next_path))
                if nx == bx - 1 and ny == by - 1:
                    return distance[nx][ny], next_path


n = int(input())
ax, ay, bx, by = map(int, input().split())
k = int(input())
board = [[1] * n for _ in range(n)]

# 1. 주어진 회로를 배치
for _ in range(int(input())):
    _, *xy = map(int, input().split())
    for i in range(2, len(xy) - 1, 2):
        x1, y1, x2, y2 = xy[i - 2], xy[i - 1], xy[i], xy[i + 1]
        d1 = -1 if x1 < x2 else 1
        d2 = -1 if y1 < y2 else 1
        board[x2 - 1][y2 - 1] = k
        for dx in range(1, abs(x1 - x2) + 1):
            board[x2 + (dx * d1) - 1][y2 - 1] = k
        for dy in range(1, abs(y1 - y2) + 1):
            board[x2 - 1][y2 + (dy * d2) - 1] = k

# 2. A -> B 회로의 최소 비용 출력
min_distance, min_path = dijkstra(ax - 1, ay - 1)
print(min_distance)

sx, sy = min_path[0]
nsx, nsy = min_path[1]
is_x_direction = True if sx == nsx else False
points = []

for i in range(2, len(min_path)):
    px, py = min_path[i - 1]
    cx, cy = min_path[i]
    if is_x_direction and px != cx:
        is_x_direction = False
        points.append((px, py))
        continue
    if not is_x_direction and py != cy:
        is_x_direction = True
        points.append((px, py))

print(len(points) + 2, ax, ay, end=" ")
for x, y in points:
    print(x + 1, y + 1, end=" ")
print(bx, by)
