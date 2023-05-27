# 실버 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        print(heappop(heap) if heap else 0)
    else:
        heappush(heap, x)
