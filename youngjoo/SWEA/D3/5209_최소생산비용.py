# permutations

def recursion(depth, cost):
    global min_cost

    if cost >= min_cost:  # 가지치기
        return

    if depth == n:
        min_cost = min(cost, min_cost)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            recursion(depth + 1, cost + board[depth][i])
            visited[i] = False


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_cost = 1485  # 문제 조건 상 나올 수 있는 최대 생산 비용
    recursion(0, 0)

    print(f"#{t} {min_cost}")