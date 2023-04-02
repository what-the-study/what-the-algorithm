# 실버 2

import sys

input = sys.stdin.readline

arr = [i for i in range(250000)]

# 에라토스테네스의 체 (Sieve of Eratosthenes)
for i in range(2, 250000):
    if arr[i] > 0:
        for j in range(i + i, 250000, i):
            arr[j] = 0

while True:
    n = int(input())

    if n == 0:
        break

    print(sum(arr[i] > 0 for i in range(n + 1, n * 2 + 1)))
