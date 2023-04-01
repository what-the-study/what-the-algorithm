# 브론즈 1

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
counter = [0] * 10001

for _ in range(n):
    counter[int(input())] += 1

for i in range(1, 10001):
    for _ in range(counter[i]):
        print(str(i) + "\n")
