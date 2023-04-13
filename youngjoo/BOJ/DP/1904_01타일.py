# 실버 3

n = int(input())

memo = [1, 1, 2]

for i in range(3, n + 1):
    memo.append((memo[i - 1] + memo[i - 2]) % 15746)

print(memo[n])
