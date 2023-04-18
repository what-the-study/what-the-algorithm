# 실버 2

n = int(input())
life = list(map(int, input().split()))
joy = list(map(int, input().split()))
dp = [0] * 101

for i in range(n):
    for j in range(100, life[i], -1):
        dp[j] = max(dp[j], dp[j - life[i]] + joy[i])

print(max(dp))
