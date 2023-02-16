# permutations

def recursion(depth, total):
    global min_total

    if total >= min_total:  # backtracking
        return

    if depth == n:
        min_total = min(total, min_total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            recursion(depth + 1, total + board[depth][i])
            visited[i] = False


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_total = 90
    recursion(0, 0)

    print(f"#{t} {min_total}")
