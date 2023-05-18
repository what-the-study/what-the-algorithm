# 골드 4

import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

if k < 5:
    print(0)
else:
    base = {0, 2, 8, 13, 19}  # a, c, i, n, t
    not_base = [i for i in range(26) if i not in base]
    learned = 0  # 이진 자리가 1이면 해당 알파벳 배움, 0이면 안 배움
    max_counts = 0

    # 1. 기본적으로 등장하는 a, c, i, n, t 배우기
    for i in base:
        learned |= 1 << i

    # 2. 나머지 21개 알파벳 중 임의로 뽑아서 배운 후, 검증하기
    for case in combinations(not_base, k - 5):
        # 임의로 뽑은 알파벳 배우기
        for i in case:
            learned |= 1 << i

        counts = 0

        for word in words:
            for i in range(4, len(word) - 4):
                # 해당 알파벳이 배우지 않은 알파벳이라면 break
                if learned & (1 << (ord(word[i]) - 97)) == 0:
                    break
            else:
                counts += 1

        max_counts = max(max_counts, counts)

        # 임의로 뽑은 알파벳 배우기를 취소 & 원상복구
        for i in case:
            learned &= ~(1 << i)

    print(max_counts)
