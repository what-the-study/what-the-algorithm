# 플래티넘 4

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(node):
    global label
    label += 1

    root = labels[node] = label
    stack.append(node)

    for next_node in graph[node]:
        if labels[next_node] == 0:
            root = min(root, dfs(next_node))
            continue

        if not confirmed[next_node]:
            root = min(root, labels[next_node])

    if root == labels[node]:
        group = []

        while stack:
            p = stack.pop()
            confirmed[p] = True
            scc[p] = node
            group.append(p)

            if p == node:
                break

        groups[node] = group

    return root


test = int(input())

for t in range(test):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    if t < test - 1:
        input()

    confirmed = [False] * n
    labels = [0] * n
    scc = [-1] * n
    label = 0
    stack, groups = [], {}

    for i in range(n):
        if labels[i] == 0:
            dfs(i)

    in_degree = {root: 0 for root in groups}

    for node in range(n):
        for next_node in graph[node]:
            if scc[node] != scc[next_node]:
                in_degree[scc[next_node]] += 1

    if list(in_degree.values()).count(0) > 1:
        print("Confused")
    else:
        for root in in_degree:
            if in_degree[root] == 0:
                print(*sorted(groups[root]), sep="\n")
                break

    print()
