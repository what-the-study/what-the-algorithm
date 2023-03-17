# 골드 3

import sys

input = sys.stdin.readline
INF = 99999999


def bellman_ford():
    distance = [INF] * (n + 1)

    for i in range(n):
        is_updated = False

        for s, e, t in edges:
            next_dist = distance[s] + t
            if next_dist < distance[e]:
                if i == n - 1:
                    return "YES"
                is_updated = True
                distance[e] = next_dist

        if not is_updated:
            break

    return "NO"


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print(bellman_ford())
