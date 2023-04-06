# 실버 3

import sys


def divide(n):
    if n == 1:
        return "-"
    return divide(n // 3) + " " * (n // 3) + divide(n // 3)


lines = sys.stdin.readlines()

for line in lines:
    n = int(line)
    print(divide(3 ** n))
