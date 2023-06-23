# 플래티넘 4

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(node):
    global label
    label += 1

    labels[node] = label
    root = label
    stack.append(node)

    for next_node in graph[node]:
        if labels[next_node] == 0:
            root = min(root, dfs(next_node))
            continue

        if not confirmed[next_node]:
            root = min(root, labels[next_node])

    if root == labels[node]:
        while stack:
            p = stack.pop()
            confirmed[p] = True
            group[p] = node

            if p == node:
                break

    return root


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)

    confirmed = [False] * (n + 1)
    labels = [0] * (n + 1)
    label = 0
    stack = []
    group = [0] * (n + 1)

    for i in range(1, n + 1):
        if labels[i] == 0:
            dfs(i)

    in_degree = defaultdict(int)

    for node in range(1, n + 1):
        for next_node in graph[node]:
            if group[node] != group[next_node]:
                in_degree[group[next_node]] += 1

    print(len(set(group[1:])) - len(in_degree))
