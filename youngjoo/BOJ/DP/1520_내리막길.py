# 골드 3

import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and heights[x][y] > heights[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


m, n = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]  # 0이 아닌 -1로 초기화 해야 함에 주의

dp[-1][-1] = 1
dfs(0, 0)

print(dp[0][0])
