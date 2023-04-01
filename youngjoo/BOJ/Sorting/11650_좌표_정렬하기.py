# 실버 5

import sys

input = sys.stdin.readline

n = int(input())
xy = sorted(tuple(map(int, input().split())) for _ in range(n))
for x, y in xy:
    print(x, y)