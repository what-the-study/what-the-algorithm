# 골드 5

import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack, result = [], []

for i, tower in enumerate(towers):
    while stack and stack[-1][0] <= tower:
        stack.pop()

    result.append(0 if not stack else stack[-1][1])
    stack.append((tower, i + 1))

print(*result)
