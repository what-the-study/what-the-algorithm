# 실버 3

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = set(input() for _ in range(n))
print(sum(input() in s for _ in range(m)))
