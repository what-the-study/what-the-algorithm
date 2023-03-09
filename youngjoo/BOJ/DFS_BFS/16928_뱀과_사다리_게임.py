# 골드 5

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    visited = [0] * 101
    queue = deque([start])

    while queue:
        number = queue.popleft()
        for i in range(1, 7):
            next_number = number + i
            if next_number <= 100:
                if moves[next_number] > 0:
                    next_number = moves[next_number]
                if visited[next_number] == 0:
                    visited[next_number] = visited[number] + 1
                    queue.append(next_number)

    return visited[100]


n, m = map(int, input().split())
moves = [0] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    moves[a] = b

print(bfs(1))
