# 골드 5

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x_root, y_root = find(x), find(y)
    parent[y_root] = x_root


n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    ops, a, b = map(int, input().split())

    if ops == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
