# 골드 2

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]

for i in range(1, n):
    if dp[-1] < a[i]:
        dp.append(a[i])
    else:
        index = bisect_left(dp, a[i])
        dp[index] = a[i]

print(len(dp))
