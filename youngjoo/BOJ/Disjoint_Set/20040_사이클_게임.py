# 골드 4

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = list(range(n))

for t in range(1, m + 1):
    x, y = map(int, input().split())
    x_root, y_root = find(x), find(y)

    if x_root == y_root:
        print(t)
        break

    parent[y_root] = x_root
else:
    print(0)
