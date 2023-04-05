# 실버 4

import sys

input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    ops = input().split()

    if ops[0] == "push":
        stack.append(ops[1])
    elif ops[0] == "top":
        print(stack[-1] if stack else -1)
    elif ops[0] == "size":
        print(len(stack))
    elif ops[0] == "empty":
        print(0 if stack else 1)
    elif ops[0] == "pop":
        print(stack.pop() if stack else -1)
