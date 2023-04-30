# 골드 1

import sys
from collections import deque

input = sys.stdin.readline
EMPTY, WALL, PAPER = ".", "*", "$"
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    papers = 1 if maze[x][y] == PAPER else 0
    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                now = maze[nx][ny]
                if now == WALL:
                    continue  # 벽은 못감
                if now.isupper() and now not in key_set:
                    continue  # 열쇠가 없는 문은 못감
                if now.islower():
                    key_set.add(now.upper())
                if now == PAPER:
                    papers += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return papers


for _ in range(int(input())):
    h, w = map(int, input().split())
    doors = []
    maze = []

    # 1. 빌딩 정보 입력, 입구 좌표 저장
    for i in range(h):
        line = input().rstrip()
        maze.append(line)
        if i == 0 or i == h - 1:
            # 맨 위층, 맨 아래층 입구 좌표 저장
            for j in range(w):
                if line[j] != WALL:
                    doors.append((i, j))
        else:
            # 중간 층 입구 좌표 저장
            if line[0] != WALL:
                doors.append((i, 0))
            if line[-1] != WALL:
                doors.append((i, w - 1))

    # 2. 열쇠 입력
    keys = input().rstrip()
    key_set = {key.upper() for key in keys} if keys != "0" else set()
    key_counts = len(key_set)

    # 3. 열쇠 먼저 모두 주워 담기
    while True:
        visited = [[False] * w for _ in range(h)]

        for sx, sy in doors:
            start = maze[sx][sy]
            if start.isupper() and start not in key_set:
                continue
            if start.islower():
                key_set.add(start.upper())
            bfs(sx, sy)

        # 더이상 주울 키가 없으면 탈출
        if len(key_set) == key_counts:
            break

        key_counts = len(key_set)

    # 4. 마지막 한번의 BFS를 통해 문서를 최대한 많이 줍기
    visited = [[False] * w for _ in range(h)]
    max_papers = 0

    for sx, sy in doors:
        # 이미 방문한 적 있는 입구나 열쇠가 없는 문으로 시작하는 입구는 탐색할 필요 없음
        if visited[sx][sy] or (maze[sx][sy].isupper() and maze[sx][sy] not in key_set):
            continue

        max_papers += bfs(sx, sy)

    print(max_papers)
