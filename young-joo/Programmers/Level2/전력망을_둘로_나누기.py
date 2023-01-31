# 완전탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/86971)

def solution(n, wires):
    def search(node):
        visited[node] = True
        for next_node in tree[node]:
            if not visited[next_node]:
                nonlocal tower
                tower += 1
                search(next_node)

    min_diff = n

    for i in range(len(wires)):
        new_wires = [wire for j, wire in enumerate(wires) if i != j]
        visited = [False] * (n + 1)
        tree = [[] for _ in range(n + 1)]
        for s, e in new_wires:
            tree[s].append(e)
            tree[e].append(s)

        tower_counts = []
        for j in range(1, n + 1):
            if not visited[j]:
                tower = 1
                search(j)
                tower_counts.append(tower)

        min_diff = min(min_diff, abs(tower_counts[0] - tower_counts[1]))

    return min_diff


print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
