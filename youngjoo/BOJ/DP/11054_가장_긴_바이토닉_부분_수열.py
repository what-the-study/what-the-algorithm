# 골드 4

n = int(input())
a = list(map(int, input().split()))
dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if a[-j - 1] < a[-i - 1]:
            dp2[-i - 1] = max(dp2[-i - 1], dp2[-j - 1] + 1)

print(max(dp1[i] + dp2[i] for i in range(n)) - 1)
