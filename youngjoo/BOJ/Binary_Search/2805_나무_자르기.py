# 실버 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
heights = sorted(map(int, input().split()))
start, end = 0, heights[-1]
max_height = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(n - 1, -1, -1):
        if heights[i] <= mid:
            break
        total += heights[i] - mid

    if m <= total:
        start = mid + 1
        max_height = max(max_height, mid)
    else:
        end = mid - 1

print(max_height)