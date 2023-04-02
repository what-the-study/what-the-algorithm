# 실버 3

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [i for i in range(n + 1)]

# 에라토스테네스의 체 (Sieve of Eratosthenes)
for i in range(2, n + 1):
    if arr[i] > 0:
        for j in range(i + i, n + 1, i):
            arr[j] = 0

for i in range(m, n + 1):
    if i > 1 and arr[i] > 0:
        print(arr[i])
