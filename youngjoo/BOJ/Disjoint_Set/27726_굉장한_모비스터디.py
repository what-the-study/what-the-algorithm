# 골드 2

import sys
from collections import defaultdict

input = sys.stdin.readline


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    x_root, y_root = find(x, parent), find(y, parent)

    if x_root != y_root:
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1


n = int(input())
parents = [list(range(n + 1)) for _ in range(3)]
ranks = [[0] * (n + 1) for _ in range(3)]

# 1. 세 번의 스터디에 대한 유니온 파인드
for i, m in enumerate(map(int, input().split())):
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b, parents[i], ranks[i])

# 2. 경로 압축으로 루트 최신화
for i in range(1, n + 1):
    for j in range(3):
        find(i, parents[j])

# 3. 세 번의 스터디의 루트 원소가 같은 직원들끼리 굉장한 모비스터디 형성
table = list(zip(*parents))
table_dict = defaultdict(list)

for i in range(1, n + 1):
    table_dict[table[i]].append(i)

# 4. 2명 이상의 굉장한 모비스터디를 정렬하고 출력
answer = sorted(sorted(study) for study in table_dict.values() if len(study) >= 2)

print(len(answer))
for study in answer:
    print(*study)
