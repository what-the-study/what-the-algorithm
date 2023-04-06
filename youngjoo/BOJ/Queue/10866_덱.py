# 실버 4

import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
    ops = input().split()

    if ops[0] == "push_front":
        queue.appendleft(ops[1])
    elif ops[0] == "push_back":
        queue.append(ops[1])
    elif ops[0] == "pop_front":
        print(queue.popleft() if queue else -1)
    elif ops[0] == "pop_back":
        print(queue.pop() if queue else -1)
    elif ops[0] == "size":
        print(len(queue))
    elif ops[0] == "empty":
        print(0 if queue else 1)
    elif ops[0] == "front":
        print(queue[0] if queue else -1)
    elif ops[0] == "back":
        print(queue[-1] if queue else -1)