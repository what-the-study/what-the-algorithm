# Two-dimentional lists

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 우/하/좌/상

for t in range(1, int(input()) + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x, y, k = 0, 0, 0

    for i in range(1, n * n + 1):
        snail[x][y] = i
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            k = (k + 1) % 4
            x += dx[k]
            y += dy[k]

    print(f"#{t}", *[" ".join(map(str, line)) for line in snail], sep="\n")
