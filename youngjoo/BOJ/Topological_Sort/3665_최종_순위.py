# 골드 1

import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in range(1, n + 1):
            if graph[next_node][node] == 0:
                continue
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)


for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # 작년 순위 반영
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[t[j]][t[i]] = 1

    # 올해 순위 변경 반영
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b], graph[b][a] = graph[b][a], graph[a][b]

    in_degree = [sum(graph[i]) for i in range(n + 1)]
    result = []

    topology_sort()

    if len(result) < n:
        print("IMPOSSIBLE")
    else:
        print(*result)
