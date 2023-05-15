# 골드 4

import sys

input = sys.stdin.readline
INF = 9999999

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = INF

for r in range(3):
    temp = list(board[0])
    board[0] = [board[0][k] if r == k else INF for k in range(3)]
    dp = [[-1] * 3 for _ in range(n + 1)]
    dp[0] = [0] * 3

    for i in range(1, n + 1):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][k] for k in range(3) if j != k and dp[i - 1][k] > -1) + board[i - 1][j]

    answer = min(answer, min(cost for k, cost in enumerate(dp[-1]) if r != k))
    board[0] = temp

print(answer)
