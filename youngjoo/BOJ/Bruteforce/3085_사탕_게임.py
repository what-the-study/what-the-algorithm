# 실버 3

import sys

input = sys.stdin.readline


def get_max_in_line(board):
    max_counts = 1

    for line in board:
        standard_color = line[0]
        counts = 1

        for color in line[1:]:
            if color == standard_color:
                counts += 1
            else:
                standard_color = color
                max_counts = max(max_counts, counts)
                counts = 1

        max_counts = max(max_counts, counts)

    return max_counts


def get_max_in_board():
    max_candy = max(get_max_in_line(board), get_max_in_line(list(zip(*board))))

    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[x][y] != board[nx][ny]:
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    max_candy = max(get_max_in_line(board), get_max_in_line(list(zip(*board))), max_candy)
                    if max_candy == n:
                        return max_candy
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

    return max_candy


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
print(get_max_in_board())
