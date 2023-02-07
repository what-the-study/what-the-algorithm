# Two-dimensional lists

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_total = 0

    for x in range(n - m + 1):
        for y in range(n - m + 1):
            total = sum(board[i][j] for i in range(x, x + m) for j in range(y, y + m))
            max_total = max(total, max_total)

    print(f"#{t} {max_total}")
