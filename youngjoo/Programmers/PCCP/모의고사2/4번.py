from collections import deque


def solution(n, m, hole):
    def bfs(x, y):
        queue = deque([(x, y, False, 0)])
        visited_with_shoes[x][y] = True
        visited_without_shoes[x][y] = True

        while queue:
            x, y, used_shoes, counts = queue.popleft()
            now_visited = visited_with_shoes if used_shoes else visited_without_shoes

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 1 <= nx <= m and 1 <= ny <= n and not now_visited[nx][ny] and board[nx][ny] == 1:
                    if nx == m and ny == n:
                        return counts + 1
                    now_visited[nx][ny] = True
                    queue.append((nx, ny, used_shoes, counts + 1))

                if not used_shoes:
                    nx += dx[i]
                    ny += dy[i]

                    if 1 <= nx <= m and 1 <= ny <= n and not visited_with_shoes[nx][ny] and board[nx][ny] == 1:
                        if nx == m and ny == n:
                            return counts + 1
                        visited_with_shoes[nx][ny] = True
                        queue.append((nx, ny, True, counts + 1))

        return -1

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = [[1] * (n + 1) for _ in range(m + 1)]
    visited_with_shoes = [[False] * (n + 1) for _ in range(m + 1)]
    visited_without_shoes = [[False] * (n + 1) for _ in range(m + 1)]

    for a, b in hole:
        board[b][a] = 0

    return bfs(1, 1)
