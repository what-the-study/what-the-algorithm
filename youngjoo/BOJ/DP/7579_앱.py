# 골드 3

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
k = sum(cost)
dp = [0] * (k + 1)

for i in range(n):
    for j in range(k, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + memory[i])

for i, c in enumerate(dp):
    if c >= m:
        print(i)
        break
