# 플래티넘 4

import sys

input = sys.stdin.readline

board_size, pattern = int(input()), input().rstrip()
table = [0]
i = 0

for j in range(1, len(pattern)):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i - 1]

    if pattern[i] == pattern[j]:
        i += 1

    table.append(i)

print(board_size - table[-1])
