# 실버 1

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        print(heappop(heap)[1] if heap else 0)
    else:
        heappush(heap, (abs(x), x))
