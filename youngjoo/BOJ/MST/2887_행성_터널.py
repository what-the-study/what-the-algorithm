# 플래티넘 5

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


n = int(input())
planets = [list(map(lambda x: (int(x), i), input().split())) for i in range(n)]
xyz = list(map(sorted, zip(*planets)))
edges = sorted((abs(axis[i][0] - axis[i + 1][0]), axis[i][1], axis[i + 1][1]) for i in range(n - 1) for axis in xyz)

parent = list(range(n))
counts, cost = 0, 0

for w, s, e in edges:
    s_root, e_root = find(s), find(e)

    if s_root != e_root:
        parent[e_root] = s_root
        cost += w
        counts += 1

        if counts >= n - 1:
            break

print(cost)
