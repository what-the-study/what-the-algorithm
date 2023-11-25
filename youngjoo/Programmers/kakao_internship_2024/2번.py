# 2. 도넛, 막대, 8자 그래프

from collections import defaultdict, deque


def solution(edges):
    def bfs(node):
        queue = deque([node])
        visited[node] = True

        while queue:
            node = queue.popleft()

            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    graph = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    all_nodes = set()
    answer = [0, 0, 0, 0]

    for s, e in edges:
        graph[s].append(e)
        indegree[e] += 1
        outdegree[s] += 1
        all_nodes.add(s)
        all_nodes.add(e)

    # 1. 생성한 정점 찾기
    for node in all_nodes:
        if indegree[node] == 0 and outdegree[node] >= 2:
            answer[0] = node
            break

    # 2. 생성한 정점 삭제하여 그래프들을 분리
    for next_node in graph[answer[0]]:
        indegree[next_node] -= 1

    all_nodes.remove(answer[0])

    # 3. 도넛, 막대, 8자 그래프 찾기
    visited = {node: False for node in all_nodes}

    for node in all_nodes:
        if visited[node]:
            continue

        if indegree[node] == 0 and outdegree[node] >= 0:
            bfs(node)
            answer[2] += 1  # 막대 그래프
            continue

        if indegree[node] == 2 and outdegree[node] == 2:
            bfs(node)
            answer[3] += 1  # 8자 그래프
            continue

    for node in all_nodes:
        if visited[node]:
            continue

        bfs(node)
        answer[1] += 1  # 도넛 그래프

    return answer


print(solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8]]))
