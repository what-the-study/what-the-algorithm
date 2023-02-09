# Two-dimensional lists

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_flower = 0

    for x in range(n):
        for y in range(m):
            flower = board[x][y]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    flower += board[nx][ny]

            max_flower = max(flower, max_flower)

    print(f"#{t} {max_flower}")
