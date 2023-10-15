# 골드 5

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
houses, chickens = [], []
result = 99999999

for i in range(n):
    line = list(map(int, input().split()))

    for j in range(n):
        if line[j] == 1:
            houses.append((i, j))
        elif line[j] == 2:
            chickens.append((i, j))

for case in combinations(chickens, m):
    result = min(result, sum(min(abs(hx - cx) + abs(hy - cy) for cx, cy in case) for hx, hy in houses))

print(result)
