# 골드 4

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))
start, end = 1, houses[-1] - houses[0]
max_dist = 1

while start <= end:
    mid = (start + end) // 2
    counts, temp = 1, houses[0] + mid

    for house in houses:
        if house >= temp:
            counts += 1
            temp = house + mid

    if counts >= c:
        max_dist = max(mid, max_dist)
        start = mid + 1
    else:
        end = mid - 1

print(max_dist)
