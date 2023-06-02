# 골드 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
minutes = list(map(int, input().split()))

if n <= m:
    print(n)
elif m == 1:
    print(1)
else:
    start, end = 1, n * max(minutes)
    standard = 0

    while start <= end:
        mid = (start + end) // 2
        total = m + sum(mid // minute for minute in minutes)

        if total < n:
            start = mid + 1
        else:
            standard = mid
            end = mid - 1

    prev = m + sum((standard - 1) // minute for minute in minutes)

    for i, minute in enumerate(minutes):
        if standard % minute == 0:
            prev += 1

        if prev == n:
            print(i + 1)
            break
