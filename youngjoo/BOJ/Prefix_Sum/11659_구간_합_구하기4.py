# 실버 3

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
