# 실버 1

import sys

input = sys.stdin.readline

s = input().rstrip()
prefix = dict.fromkeys(s)

for key in prefix:
    prefix[key] = [0]

for char in s:
    for key in prefix:
        prev = prefix[key][-1]
        prefix[key].append(prev + 1 if char == key else prev)

for _ in range(int(input())):
    char, *section = input().split()
    l, r = map(int, section)
    if char not in prefix:
        print(0)
    else:
        print(prefix[char][r + 1] - prefix[char][l])
