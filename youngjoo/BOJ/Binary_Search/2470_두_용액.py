# 골드 5

import sys

input = sys.stdin.readline

n = int(input())
values = sorted(map(int, input().split()))
i, j = 0, n - 1
first, second = values[i], values[j]
answer = abs(first + second)

while i < j:
    total = values[i] + values[j]

    if abs(total) < answer:
        first, second = values[i], values[j]
        answer = abs(total)

    if total == 0:
        break

    if total > 0:
        j -= 1
    else:
        i += 1

print(first, second)
