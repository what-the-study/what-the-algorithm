# 플래티넘 3

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def kruskal(edges):
    counts, total = 0, 0

    for w, x, y in edges:
        x_root, y_root = find(x), find(y)

        if x_root != y_root:
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root

            total += w
            counts += 1

            if counts >= n - 1:
                break

    return total


while True:
    n, m, k = map(int, input().split())

    if n == m == k == 0:
        break

    min_edges, max_edges = [], []

    for _ in range(m):
        c, f, t = input().split()
        f, t = int(f), int(t)
        cost = 1 if c == "B" else 0
        min_edges.append((cost, f, t))
        max_edges.append((-cost, f, t))

    min_edges.sort()
    max_edges.sort()

    parent = list(range(n + 1))
    min_blue = kruskal(min_edges)

    parent = list(range(n + 1))
    max_blue = -kruskal(max_edges)

    print(1 if min_blue <= k <= max_blue else 0)
