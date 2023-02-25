# 골드 5

from collections import deque


def is_blocked(x, y, index):
    for dx, dy in paths[index]:
        if x + dx == r2 and y + dy == c2:
            return True
    return False


def bfs(x, y):
    visited = [[0] * 9 for _ in range(10)]
    visited[x][y] = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for index, dxy in enumerate(delta):
            nx, ny = x + dxy[0], y + dxy[1]
            if 0 <= nx <= 9 and 0 <= ny <= 8 and visited[nx][ny] == 0 and not is_blocked(x, y, index):
                if nx == r2 and ny == c2:
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
delta = [(-3, -2), (-3, 2), (-2, -3), (-2, 3), (3, -2), (3, 2), (2, -3), (2, 3)]
paths = [
    [(-1, 0), (-2, -1)],
    [(-1, 0), (-2, 1)],
    [(0, -1), (-1, -2)],
    [(0, 1), (-1, 2)],
    [(1, 0), (2, 1)],
    [(1, 0), (2, -1)],
    [(0, -1), (1, -2)],
    [(0, 1), (1, 2)]
]
print(bfs(r1, c1))
