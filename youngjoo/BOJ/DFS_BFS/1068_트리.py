# 골드 5

import sys

input = sys.stdin.readline


def dfs(node):
    visited[node] = True

    for next_node in tree[node]:
        if not visited[next_node]:
            dfs(next_node)


n = int(input())
parents = list(map(int, input().split()))
m = int(input())

tree = [[] for _ in range(n)]
for child, parent in enumerate(parents):
    if parent > -1:
        tree[parent].append(child)

visited = [False] * n
dfs(m)

result = 0

for i, line in enumerate(tree):
    if visited[i]:
        continue

    if not line:
        result += 1
        continue

    for node in line:
        if not visited[node]:
            break
    else:
        result += 1

print(result)
