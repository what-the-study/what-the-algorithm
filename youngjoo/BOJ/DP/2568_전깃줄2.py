# 플래티넘 5

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
poles = sorted(tuple(map(int, input().split())) for _ in range(n))
numbers = [poles[0][1]]
counts = [1] * n

for i in range(1, n):
    if numbers[-1] < poles[i][1]:
        numbers.append(poles[i][1])
        counts[i] = len(numbers)
    else:
        index = bisect_left(numbers, poles[i][1])
        numbers[index] = poles[i][1]
        counts[i] = index + 1

max_count = max(counts)
i = n - 1
remains = []

while max_count > 0:
    if counts[i] == max_count:
        remains.append(poles[i])
        max_count -= 1
    i -= 1

removes = sorted(set(poles) - set(remains))
print(len(removes))
print(*[a for a, _ in removes], sep="\n")
