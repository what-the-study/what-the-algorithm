# 브론즈 3

import sys

input = sys.stdin.readline

while True:
    a, b, c = sorted(map(int, input().split()))

    if a == b == c == 0:
        break

    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
