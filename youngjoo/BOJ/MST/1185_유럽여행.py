# 플래티넘 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


n, p = map(int, input().split())
costs = [int(input()) for _ in range(n)]
parent = list(range(n + 1))
total, counts = 0, 0
edges = []

for _ in range(p):
    s, e, w = map(int, input().split())
    cost = w + w + costs[s - 1] + costs[e - 1]
    edges.append((cost, s, e))

edges.sort()

for cost, s, e in edges:
    s_root, e_root = find(s), find(e)

    if s_root != e_root:
        parent[e_root] = s_root
        total += cost
        counts += 1

        if counts >= n - 1:
            break

print(total + min(costs))
