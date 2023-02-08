# Two-dimensional lists

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for x in range(n):
        for y in range(n):
            total = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    total += abs(board[x][y] - board[nx][ny])

            result += total

    print(f"#{t} {result}")
