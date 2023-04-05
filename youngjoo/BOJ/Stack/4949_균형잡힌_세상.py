# 실버 4

import sys

input = sys.stdin.readline

while True:
    stack = []
    s = input().rstrip()

    if s == ".":
        break

    for i in s:
        if i in ["(", "["]:
            stack.append(i)
        elif i in [")", "]"]:
            if not stack:
                print("no")
                break

            j = stack.pop()
            if (i == ")" and j != "(") or (i == "]" and j != "["):
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
