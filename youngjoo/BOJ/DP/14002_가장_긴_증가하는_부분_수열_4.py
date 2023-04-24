# 골드 4

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
numbers = [[a[i]] for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            numbers[i] = numbers[j] + [a[i]]

max_index, max_length = 0, 0

for i, length in enumerate(dp):
    if max_length < length:
        max_index = i
        max_length = length

print(max_length)
print(*numbers[max_index])
