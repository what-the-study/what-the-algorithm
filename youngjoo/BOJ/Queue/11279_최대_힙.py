# 실버 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        print(-heappop(heap) if heap else 0)
    else:
        heappush(heap, -x)
