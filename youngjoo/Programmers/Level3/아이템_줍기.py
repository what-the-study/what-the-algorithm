# 깊이/너비 우선 탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/87694)

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상/하/좌/우
    board = [[0] * 102 for _ in range(102)]  # 잘못된 경로 방지를 위해 크기를 2배 증가

    # 1. 사각형 영역에 모두 1 표시
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                board[i][j] = 1

    # 2. 테두리를 제외한 안쪽 모두 0으로 표시
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2 + 1, x2 * 2):
            for j in range(y1 * 2 + 1, y2 * 2):
                board[i][j] = 0

    visited = [[0] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 1
    queue = deque([(characterX * 2, characterY * 2)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                if nx == itemX * 2 and ny == itemY * 2:
                    return (visited[nx][ny] - 1) // 2
                queue.append((nx, ny))


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
