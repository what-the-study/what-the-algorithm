# 실버 1

# 1. 스택 DFS 풀이
import sys

input = sys.stdin.readline

n = int(input().rstrip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

visited = [-1] * (n + 1)
visited[1] = 0
moves = 0
stack = [1]

while stack:
    node = stack.pop()
    for next_node in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[node] + 1
            if len(tree[next_node]) == 1:
                moves += visited[next_node]
                continue
            stack.append(next_node)

print("Yes" if moves % 2 == 1 else "No")

# 2. 재귀 DFS 풀이(재귀 깊이를 임의로 늘림)
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
#
#
# def dfs(node):
#     for next_node in tree[node]:
#         if visited[next_node] == -1:
#             visited[next_node] = visited[node] + 1
#             if len(tree[next_node]) == 1:
#                 global moves
#                 moves += visited[next_node]
#                 continue
#             dfs(next_node)
#
#
# n = int(input().rstrip())
# tree = [[] for _ in range(n + 1)]
#
# for _ in range(n - 1):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
#
# visited = [-1] * (n + 1)
# visited[1] = 0
# moves = 0
# dfs(1)
#
# print("Yes" if moves % 2 == 1 else "No")
