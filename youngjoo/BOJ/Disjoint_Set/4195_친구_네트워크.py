# 골드 2

import sys

input = sys.stdin.readline


def find(name):
    if name != parent[name]:
        parent[name] = find(parent[name])
    return parent[name]


for _ in range(int(input())):
    parent = {}
    counts = {}

    for _ in range(int(input())):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            counts[x] = 1

        if y not in parent:
            parent[y] = y
            counts[y] = 1

        x_root, y_root = find(x), find(y)

        if x_root != y_root:
            parent[y_root] = x_root
            counts[x_root] += counts[y_root]

        print(counts[x_root])
