# Two-dimensional lists

for _ in range(10):
    t = input()
    board = [list(map(int, input().split())) for _ in range(100)]

    row = max(map(sum, board))
    col = max(map(sum, zip(*board)))
    dia = max(map(sum, zip(*[(board[i][i], board[99 - i][i]) for i in range(100)])))

    print(f"#{t} {max(row, col, dia)}")
