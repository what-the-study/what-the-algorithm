# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


while True:
    m, n = map(int, input().split())

    if m == n == 0:
        break

    edges = []
    total = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z

    edges.sort()
    parent = list(range(m))
    counts, cost = 0, 0

    for z, x, y in edges:
        x_root, y_root = find(x), find(y)

        if x_root != y_root:
            parent[y_root] = x_root
            counts += 1
            cost += z

            if counts >= m - 1:
                break

    print(total - cost)
