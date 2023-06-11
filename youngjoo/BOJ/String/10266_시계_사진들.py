# 플래티넘 4

import sys

input = sys.stdin.readline


def make_table(pattern):
    table = [0]
    i = 0

    for j in range(n):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]

        if pattern[i] == pattern[j]:
            i += 1

        table.append(i)

    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    i = 0

    for j in range(n + n):
        while i > 0 and pattern[i] != parent[j]:
            i = table[i - 1]

        if pattern[i] == parent[j]:
            if i == n - 1:
                return "possible"
            i += 1

    return "impossible"


n = int(input())
clock1 = sorted(map(int, input().split()))
clock2 = sorted(map(int, input().split()))
angle1 = [360000 - (clock1[-1] - clock1[0])]
angle2 = [360000 - (clock2[-1] - clock2[0])]

for i in range(1, n):
    angle1.append(clock1[i] - clock1[i - 1])
    angle2.append(clock2[i] - clock2[i - 1])

angle1.extend(angle1)
table = make_table(angle2)
print(kmp(angle1, angle2))
