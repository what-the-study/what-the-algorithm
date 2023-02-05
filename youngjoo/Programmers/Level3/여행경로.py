# 깊이/너비 우선 탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/43164)

def solution(tickets):
    def dfs(node):
        if not graph[node] or all(visited for _, visited in graph[node]):
            if len(route) == len(tickets):
                routes.append(list(route))
            return

        for next_node in graph[node]:
            if not next_node[1]:
                next_node[1] = True
                route.append(next_node[0])
                dfs(next_node[0])
                next_node[1] = False
                route.pop()

    graph = {airport: [] for ticket in tickets for airport in ticket}
    for s, e in tickets:
        graph[s].append([e, False])

    route = []
    routes = []
    dfs("ICN")

    return ["ICN"] + sorted(routes)[0]

# 반례
# print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
# ['ICN', 'A', 'C', 'A', 'B', 'D']
# print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
# ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA']
