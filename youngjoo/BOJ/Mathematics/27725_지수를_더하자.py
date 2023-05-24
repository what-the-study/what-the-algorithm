# 골드 5

import sys

input = sys.stdin.readline

n = int(input())
primes = list(map(int, input().split()))
k = int(input())
answer = 0

for prime in primes:
    temp = prime
    while temp <= k:
        answer += k // temp
        temp *= prime

print(answer)
