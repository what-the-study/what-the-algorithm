# 플래티넘 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
weights, happy = [], []
dp = [0] * (m + 1)
table = [[] for _ in range(10001)]

# 무게를 어떻게 쪼갤지 표를 미리 만듦
step, temp = 0, 0
for i in range(1, 10001):
    table[i] += table[i - 1]
    if temp == 0:
        table[i] = [1] + table[i]
        temp = step
        step += 1
    else:
        table[i][temp] += 1
        temp -= 1

for _ in range(n):
    v, c, k = map(int, input().split())
    n += len(table[k]) - 1
    for counts in table[k]:
        weights.append(v * counts)
        happy.append(c * counts)

for i in range(n):
    for j in range(m, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + happy[i])

print(max(dp))
