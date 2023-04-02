# 실버 4

import sys

input = sys.stdin.readline


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    while True:
        if n > 1 and is_prime(n):
            print(n)
            break
        n += 1
