# 실버 5

n = int(input())
memo = [0, 1]

for i in range(2, n + 1):
    memo.append(memo[i - 2] + memo[i - 1])

print(memo[n])
