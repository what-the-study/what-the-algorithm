# 실버 4

import sys
from collections import Counter

input = sys.stdin.readline

_ = input()
counter = Counter(input().split())
_ = input()
numbers = input().split()

for number in numbers:
    print(counter[number], end=" ")
