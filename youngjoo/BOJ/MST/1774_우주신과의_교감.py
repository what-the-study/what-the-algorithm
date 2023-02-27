# 골드 3

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
gods = [list(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(n - 1):
    x1, y1 = gods[i]
    for j in range(i + 1, n):
        x2, y2 = gods[j]
        w = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        heappush(edges, (w, i + 1, j + 1))

parent = list(range(n + 1))
counts, cost = 0, 0

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find(x), find(y)

    if x_root != y_root:
        union(x_root, y_root)
        counts += 1

while counts < n - 1:
    w, x, y = heappop(edges)
    x_root, y_root = find(x), find(y)

    if x_root != y_root:
        union(x_root, y_root)
        cost += w
        counts += 1

print(f"{cost:.2f}")
