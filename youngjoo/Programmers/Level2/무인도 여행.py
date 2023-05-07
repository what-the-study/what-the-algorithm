# 깊이/너비 우선 탐색

from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    answer = []

    for i in range(n):
        for j in range(m):
            if visited[i][j] or maps[i][j] == "X":
                continue

            visited[i][j] = True
            queue = deque([(i, j)])
            days = int(maps[i][j])

            # BFS
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        days += int(maps[nx][ny])

            answer.append(days)

    return sorted(answer) if answer else [-1]
