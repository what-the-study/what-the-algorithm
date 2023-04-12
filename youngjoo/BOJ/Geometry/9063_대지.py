# 브론즈 3

import sys

input = sys.stdin.readline

n = int(input())
points = list(zip(*[list(map(int, input().split())) for _ in range(n)]))
result = 1

for point in points:
    p = sorted(point)
    result *= p[-1] - p[0]

print(result)
