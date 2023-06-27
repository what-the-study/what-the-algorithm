# 플래티넘 2

import sys
from collections import deque

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
        scc_nodes = []

        while stack:
            p = stack.pop()
            scc_nodes.append(p)
            confirmed[p] = True

            if p == node:
                break

        scc[node] = scc_nodes

    return root


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

atm = [0] + [int(input()) for _ in range(n)]
start, restaurant_counts = map(int, input().split())
restaurants = list(map(int, input().split()))

# 1. SCC
confirmed = [False] * (n + 1)
labels = [0] * (n + 1)
label = 0
stack, scc = [], {}
groups = [0] * (n + 1)

for i in range(1, n + 1):
    if labels[i] == 0:
        dfs(i)

for root, nodes in scc.items():
    for node in nodes:
        groups[node] = root

# 2. Topology Sort
in_degree = {root: 0 for root in scc}
scc_graph = {root: [] for root in scc}

for i in range(1, n + 1):
    for j in graph[i]:
        if groups[i] != groups[j]:
            in_degree[groups[j]] += 1
            scc_graph[groups[i]].append(groups[j])

# 2-1. start에서 도달 가능한 정점에 대해 visited에 표시 (bfs를 이용)
# 단순히 start에서 위상정렬을 하면, 가야하는 정점인데도 진입차수가 0이 되지 않아 못가는 반례가 존재함
start = groups[start]
visited = {root: False for root in scc}
visited[start] = True
queue = deque([start])

while queue:
    root = queue.popleft()
    for next_root in scc_graph[root]:
        if not visited[next_root]:
            visited[next_root] = True
            queue.append(next_root)

# 2-2. 위상정렬
queue = deque([i for i in in_degree if in_degree[i] == 0])
roots_money = {groups[root]: 0 for root in scc}
root_restaurant = {groups[r] for r in restaurants}

while queue:
    root = queue.popleft()
    money = sum(atm[node] for node in scc[root])
    if visited[root]:
        roots_money[root] += money

    for next_root in scc_graph[root]:
        in_degree[next_root] -= 1
        if visited[next_root]:
            roots_money[next_root] = max(roots_money[root], roots_money[next_root])
        if in_degree[next_root] == 0:
            queue.append(next_root)

print(max(money for root, money in roots_money.items() if root in root_restaurant))
