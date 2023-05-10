# 골드 5

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(node):
    if not visited[node]:
        visited[node] = True

        for next_node in tree[node]:
            if not visited[next_node]:
                dp[node] += dfs(next_node)

    return dp[node]


n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dp = [1] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(r)

for _ in range(q):
    print(dp[int(input())])
