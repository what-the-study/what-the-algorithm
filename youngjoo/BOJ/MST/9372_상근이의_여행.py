# 실버 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


for _ in range(int(input())):
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    edges = [list(map(int, input().split())) for _ in range(m)]
    cost = 0

    for x, y in edges:
        x_root, y_root = find(x), find(y)

        if x_root != y_root:
            parent[y_root] = x_root
            cost += 1

            if cost >= n - 1:
                break

    print(cost)
