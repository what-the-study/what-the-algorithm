# 골드 4

import sys

input = sys.stdin.readline


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root


n, m = map(int, input().split())
true_counts, *true_people = map(int, input().split())

if true_counts == 0:
    print(m)
else:
    parent = list(range(n + 1))
    for i in range(1, true_counts):
        parent[true_people[i]] = true_people[0]

    party_people = [list(map(int, input().split())) for _ in range(m)]

    for counts, *people in party_people:
        for i in range(1, counts):
            union(people[0], people[i])

    true_root = find_set(true_people[0])
    result = 0

    for _, *people in party_people:
        if true_root != find_set(people[0]):
            result += 1

    print(result)
