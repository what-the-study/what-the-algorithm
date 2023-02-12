# Two-dimentional lists

def is_correct(board):
    for line in board:
        if len(set(line)) < 9:
            return False
    return True


for t in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku3 = []
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sudoku3.append([sudoku[i][j] for i in range(x, x + 3) for j in range(y, y + 3)])

    result = is_correct(sudoku) and is_correct(list(zip(*sudoku))) and is_correct(sudoku3)
    print(f"#{t} {int(result)}")
