# 골드 5

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w, v = [], []
dp = [0] * (k + 1)

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(n):
    for j in range(k, 0, -1):
        if j < w[i]:
            break
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(max(dp))
