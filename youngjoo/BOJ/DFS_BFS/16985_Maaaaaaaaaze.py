# 골드 2

import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline


def can_move_to(x, y, z):
    return 0 <= x < n and 0 <= y < n and 0 <= z < n and cube[x][y][z] == "1"


def bfs(x, y, z):
    visited = [[[0] * n for _ in range(n)] for _ in range(n)]
    visited[x][y][z] = 1
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()
        for dx, dy, dz in delta:
            nx, ny, nz = x + dx, y + dy, z + dz
            if can_move_to(nx, ny, nz) and visited[nx][ny][nz] == 0:
                if nx == ny == nz == n - 1:
                    if visited[x][y][z] == 12:
                        print(12)
                        exit()
                    return visited[x][y][z]
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))

    return -1


def recursion(depth):
    if depth == n:
        if cube[0][0][0] == "0" or cube[n - 1][n - 1][n - 1] == "0":
            return
        move_counts = bfs(0, 0, 0)
        if move_counts != -1:
            global min_move_counts
            min_move_counts = min(move_counts, min_move_counts)
        return

    for i in range(4):
        recursion(depth + 1)
        cube[depth] = [line[::-1] for line in zip(*cube[depth])]  # 판 90도 회전


n = 5
squares = [[input().split() for _ in range(n)] for _ in range(n)]
delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]  # (dx, dy, dz)
min_move_counts = 125

for case in permutations(squares):
    cube = list(case)
    recursion(0)

print(min_move_counts if min_move_counts < 125 else -1)
