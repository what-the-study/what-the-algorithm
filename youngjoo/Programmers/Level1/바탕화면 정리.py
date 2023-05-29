def get_point(board, start, end, step=1):
    for point in range(start, end, step):
        if any(board[point]):
            return point


def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    is_files = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                is_files[i][j] = True

    is_files_col = list(zip(*is_files))

    lux = get_point(is_files, 0, n)
    luy = get_point(is_files_col, 0, m)
    rdx = get_point(is_files, n - 1, -1, -1) + 1
    rdy = get_point(is_files_col, m - 1, -1, -1) + 1

    return [lux, luy, rdx, rdy]
