# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


n = int(input())
parent = list(range(n + 1))
edges = []
cost, counts = 0, 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i + 1, n):
        edges.append((line[j], i + 1, j + 1))
        edges.append((line[j], j + 1, i + 1))

edges.sort()

for w, s, e in edges:
    s_root, e_root = find(s), find(e)

    if s_root != e_root:
        parent[e_root] = s_root
        cost += w
        counts += 1

        if counts >= n - 1:
            break

print(cost)
