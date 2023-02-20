# 실버 1

import sys

input = sys.stdin.readline


def dfs(x, y, total):
    if total >= k:
        if x == 0 and y == c - 1:
            global result
            result += 1
        return

    if x == 0 and y == c - 1:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] == ".":
            visited[nx][ny] = True
            dfs(nx, ny, total + 1)
            visited[nx][ny] = False


r, c, k = map(int, input().split())
maps = [input().rstrip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

visited[r - 1][0] = True
dfs(r - 1, 0, 1)

print(result)
