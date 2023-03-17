# 골드 4

import sys

input = sys.stdin.readline
INF = 99999999


def bellman_ford(start):
    distance[start] = 0

    for i in range(n):
        for s, e, w in edges:
            next_dist = distance[s] + w
            if distance[s] < INF and next_dist < distance[e]:
                if i == n - 1:
                    return True
                distance[e] = next_dist

    return False


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
distance = [INF] * (n + 1)

is_negative_cycle = bellman_ford(1)

if is_negative_cycle:
    print(-1)
else:
    for city in range(2, n + 1):
        print(distance[city] if distance[city] < INF else -1)
