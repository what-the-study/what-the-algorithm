# 실버 5

import sys

input = sys.stdin.readline

n = int(input())
info = [input().split() for _ in range(n)]
for age, name in sorted(info, key=lambda x: int(x[0])):
    print(age, name)