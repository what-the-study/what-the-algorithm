# 실버 1

import sys

input = sys.stdin.readline


def quad(x1, y1, x2, y2):
    if x1 == x2 - 1 and y1 == y2 - 1:
        return board[x1][y1]

    nx = x1 + (x2 - x1) // 2
    ny = y1 + (y2 - y1) // 2

    a = quad(x1, y1, nx, ny)
    b = quad(x1, ny, nx, y2)
    c = quad(nx, y1, x2, ny)
    d = quad(nx, ny, x2, y2)

    if a == b == c == d and len(a) == 1:
        return a

    return f"({a}{b}{c}{d})"


n = int(input())
board = [input().rstrip() for _ in range(n)]
print(quad(0, 0, n, n))
