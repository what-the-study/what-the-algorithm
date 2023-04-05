# 실버 3

import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
counter = Counter(words)
result = sorted(set(words), key=lambda x: (-counter[x], -len(x), x))

for word in result:
    if len(word) >= m:
        print(word)
