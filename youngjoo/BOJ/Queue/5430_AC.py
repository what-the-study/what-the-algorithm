# 골드 5

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1]
    numbers = deque(map(int, x.split(","))) if x else []
    is_reverse = False

    for ops in p:
        if ops == "R":
            is_reverse = not is_reverse
        else:
            if not numbers:
                print("error")
                break
            if is_reverse:
                numbers.pop()
            else:
                numbers.popleft()
    else:
        if is_reverse:
            numbers.reverse()
        print(f"[{','.join(map(str, numbers))}]")
