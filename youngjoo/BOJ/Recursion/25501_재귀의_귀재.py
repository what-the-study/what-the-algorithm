# 브론즈 2

import sys

input = sys.stdin.readline


def recursion(s, l, r):
    if l >= r:
        return 1
    if s[l] != s[r]:
        return 0
    global counts
    counts += 1
    return recursion(s, l + 1, r - 1)


for _ in range(int(input())):
    s = input().rstrip()
    counts = 1
    print(recursion(s, 0, len(s) - 1), counts)
