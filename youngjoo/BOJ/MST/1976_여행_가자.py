# 골드 4

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x_root, y_root = find(x), find(y)

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


n, m = int(input()), int(input())
parent = list(range(n + 1))

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == "1":
            union(i + 1, j + 1)

plan = list(map(int, input().split()))

for i in range(m - 1):
    if parent[plan[i]] != parent[plan[i + 1]]:
        print("NO")
        break
else:
    print("YES")
