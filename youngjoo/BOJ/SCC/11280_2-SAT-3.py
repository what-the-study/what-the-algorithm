# 플래티넘 4

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(node):
    global label, is_possible
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

            if p + node == 0:
                is_possible = False  # 모순 명제 등장 시, 충족 불가능

            if p == node:
                break

    return root


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    graph[-i].append(j)
    graph[-j].append(i)

confirmed = {i: False for i in range(-n, n + 1)}
labels = {i: 0 for i in range(-n, n + 1)}
label = 0
stack = []

for i in range(-n, n + 1):
    if i != 0 and labels[i] == 0:
        is_possible = True
        dfs(i)

        if not is_possible:
            print(0)
            break
else:
    print(1)
