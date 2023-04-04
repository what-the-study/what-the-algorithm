# 실버 4

import sys

input = sys.stdin.readline

result = 0

for _ in range(int(input())):
    s = input().rstrip()

    if s == "ENTER":
        user = set()
        continue

    if s not in user:
        user.add(s)
        result += 1

print(result)
