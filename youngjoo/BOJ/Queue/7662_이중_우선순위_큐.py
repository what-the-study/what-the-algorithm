# 골드 4

import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def pop_value(heap, i):
    while True:
        key = heappop(heap) * i
        if counts[key] > 0:
            counts[key] -= 1
            return key


for _ in range(int(input())):
    min_heap, max_heap = [], []
    counts = {}
    length = 0

    for _ in range(int(input())):
        ops, n = input().split()
        n = int(n)

        if ops == "I":
            heappush(min_heap, n)
            heappush(max_heap, -n)
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
            length += 1
        elif length > 0:
            if n == -1:
                pop_value(min_heap, 1)
            else:
                pop_value(max_heap, -1)
            length -= 1

    if length == 0:
        print("EMPTY")
    elif length == 1:
        answer = pop_value(min_heap, 1)
        print(answer, answer)
    else:
        print(pop_value(max_heap, -1), pop_value(min_heap, 1))
