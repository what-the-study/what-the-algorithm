# 깊이/너비 우선 탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/1844)

from collections import deque


def solution(maps):
    def bfs(x, y):
        visited = [[0] * m for _ in range(n)]
        visited[x][y] = 1
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    if nx == n - 1 and ny == m - 1:
                        return visited[nx][ny]
                    queue.append((nx, ny))

        return -1

    n, m = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    return bfs(0, 0)
