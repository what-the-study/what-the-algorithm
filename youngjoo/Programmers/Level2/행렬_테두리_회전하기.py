def solution(rows, columns, queries):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    board = [[0] * columns for _ in range(rows)]
    result = []
    number = 1

    for i in range(rows):
        for j in range(columns):
            board[i][j] = number
            number += 1

    for query in queries:
        sx, sy, ex, ey = map(lambda x: x - 1, query)
        prev = min_number = board[sx][sy]
        board[sx][sy] = board[sx + 1][sy]
        x, y = sx, sy + 1
        direction = 0

        while x != sx or y != sy:
            prev, board[x][y] = board[x][y], prev
            min_number = min(min_number, prev)

            dx, dy = dxy[direction]
            nx, ny = x + dx, y + dy

            if sx <= nx <= ex and sy <= ny <= ey:
                x, y = nx, ny
            else:
                direction = (direction + 1) % 4
                dx, dy = dxy[direction]
                x, y = x + dx, y + dy

        result.append(min_number)

    return result
