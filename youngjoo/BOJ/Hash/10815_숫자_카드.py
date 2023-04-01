# 실버 5

import sys

input = sys.stdin.readline

_ = input()
numbers = set(input().split())
_ = input()
check = input().split()

for c in check:
    print(int(c in numbers), end=" ")
