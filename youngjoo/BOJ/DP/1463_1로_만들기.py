# 실버3

n = int(input())
memo = [0, 0]

for i in range(2, n + 1):
    temp = [memo[i - 1]]

    if i % 3 == 0:
        temp.append(memo[i // 3])
    if i % 2 == 0:
        temp.append(memo[i // 2])

    temp.sort()
    memo.append(temp[0] + 1)

print(memo[n])
