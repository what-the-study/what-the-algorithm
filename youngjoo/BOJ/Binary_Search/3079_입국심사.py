# 골드 5

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]
min_time = min(t)
start, end = min_time, min_time * m

while start <= end:
    mid = (start + end) // 2
    total = sum(mid // k for k in t)

    if total >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
