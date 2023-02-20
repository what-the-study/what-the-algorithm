# 골드 5

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x, y, visited, status):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and status[grid[x][y]] == status[grid[nx][ny]] and not visited[nx][ny]:
            dfs(nx, ny, visited, status)


n = int(input().rstrip())
grid = [input().rstrip() for _ in range(n)]
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
normal = {'R': 3, 'B': 2, 'G': 1}
weak = {'R': 2, 'B': 1, 'G': 2}
count1, count2 = 0, 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(i, j, visited1, normal)
            count1 += 1
        if not visited2[i][j]:
            dfs(i, j, visited2, weak)
            count2 += 1

print(count1, count2)
