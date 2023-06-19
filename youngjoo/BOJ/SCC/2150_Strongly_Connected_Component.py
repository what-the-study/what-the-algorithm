# 플래티넘 5

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(node):
    global label
    label += 1  # 노드 방문 때마다 라벨 번호 1 증가

    labels[node] = label  # 해당 노드에 고유 라벨 번호 부여
    root = label  # 일단 자기 자신을 SCC 루트 노드로 가정
    stack.append(node)  # 방문 노드를 스택에 삽입

    for next_node in graph[node]:
        # 1. 아직 방문 안한 곳을 탐색하면서 SCC 루트 노드 갱신
        if labels[next_node] == 0:
            root = min(root, dfs(next_node))
            continue

        # 2. 방문은 했는데, 루트 노드가 확정이 안된 곳은 사이클이란 의미이므로 SCC 루트 노드 갱신
        if not confirmed[next_node]:
            root = min(root, labels[next_node])

    # 자기 자신이 루트 노드라면 (자기의 라벨 번호가 루트 노드 번호라면)
    # 현재 노드를 루트로 SCC를 만족하므로, 스택에서 루트가 나올 때까지 하나씩 꺼내면서
    # 같은 SCC 묶음으로 담고, 확정 처리까지 진행한다.
    if root == labels[node]:
        scc_nodes = []  # 같은 SCC 묶음

        while stack:
            p = stack.pop()
            scc_nodes.append(p)
            confirmed[p] = True

            if p == node:
                break  # 자기 자신이 나왔을 때 까지만 진행

        answer.append(sorted(scc_nodes))

    return root


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

confirmed = [False] * (v + 1)  # 특정 노드의 SCC 확정 여부
labels = [0] * (v + 1)  # 각 노드의 고유 라벨 번호 (방문 여부 저장)
label = 0  # 라벨 번호를 매기기 위한 증가 변수
stack, answer = [], []

for node in range(1, v + 1):
    if labels[node] == 0:  # 아직 방문 안한 노드에 대해 DFS
        dfs(node)

print(len(answer))
for scc_nodes in sorted(answer):
    print(*scc_nodes, end=" -1\n")
