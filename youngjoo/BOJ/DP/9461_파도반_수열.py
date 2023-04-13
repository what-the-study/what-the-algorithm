# 실버 3

import sys

input = sys.stdin.readline

memo = [1, 1, 1]

for _ in range(int(input())):
    n = int(input())

    if len(memo) < n:
        for i in range(len(memo), n):
            memo.append(memo[i - 3] + memo[i - 2])

    print(memo[n - 1])
