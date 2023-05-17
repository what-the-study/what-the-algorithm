# 골드 3

import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    queue = deque()
    total_delay = [0] * (n + 1)

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            total_delay[i] = delay[i - 1]

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            in_degree[next_node] -= 1
            total_delay[next_node] = max(total_delay[next_node], total_delay[node] + delay[next_node - 1])
            if in_degree[next_node] == 0:
                queue.append(next_node)

    return total_delay[w]


for _ in range(int(input())):
    n, k = map(int, input().split())
    delay = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    w = int(input())

    print(topology_sort())
