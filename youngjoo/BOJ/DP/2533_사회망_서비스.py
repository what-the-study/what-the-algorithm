# 골드 3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(node):
    for next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            if not dfs(next_node):
                is_early_adopter[node] = True

    return is_early_adopter[node]


n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
is_early_adopter = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited[1] = True
dfs(1)

print(is_early_adopter.count(True))
