# 실버 4

import sys

input = sys.stdin.readline

people = {"ChongChong"}

for _ in range(int(input())):
    s, e = input().split()

    if s in people or e in people:
        people.update((s, e))

print(len(people))
