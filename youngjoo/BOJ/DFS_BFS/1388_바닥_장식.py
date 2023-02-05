# 실버 4

import sys

input = sys.stdin.readline


def dfs(x, y):
    if shape == "-":
        nx, ny = x, y + 1
    else:
        nx, ny = x + 1, y

    if nx < n and ny < m and not visited[nx][ny] and floor[nx][ny] == shape:
        visited[nx][ny] = True
        dfs(nx, ny)


n, m = map(int, input().split())
floor = [input().rstrip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            shape = floor[i][j]
            dfs(i, j)
            result += 1

print(result)
