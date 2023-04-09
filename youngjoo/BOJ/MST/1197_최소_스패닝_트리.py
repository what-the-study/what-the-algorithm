# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


v, e = map(int, input().split())
parent = list(range(v + 1))
edges = []
counts, cost = 0, 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for c, a, b in edges:
    a_root, b_root = find(a), find(b)

    if a_root != b_root:
        parent[b_root] = a_root  # union
        cost += c
        counts += 1

        if counts >= v - 1:  # (정점 - 1)개 만큼 간선이 모인 경우 더 탐색할 필요 없음
            break

print(cost)
