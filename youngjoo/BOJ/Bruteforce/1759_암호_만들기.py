# 골드 5

import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
chars = sorted(input().split())
vowels = "aeiou"

for case in combinations(chars, l):
    vowel_count = sum(char in vowels for char in case)

    if vowel_count >= 1 and l - vowel_count >= 2:
        print("".join(case))
