# 골드 4

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(1, n):
    for j in range(n - i):
        s, e = j, i + j
        if a[s] == a[e] and (i == 1 or dp[s + 1][e - 1] == 1):
            dp[s][e] = 1
        else:
            dp[s][e] = 0

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
