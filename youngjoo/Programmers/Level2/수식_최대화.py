# 수식 최대화

import re
from itertools import permutations

CALCULATION = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}

TYPES = "-+*"


def to_postfix(numbers, operators, priority):
    stack, postfix = [], []

    for i in range(len(operators)):
        postfix.append(numbers[i])

        while stack and priority[operators[i]] <= priority[stack[-1]]:
            postfix.append(stack.pop())

        stack.append(operators[i])

    postfix.append(numbers[-1])

    while stack:
        postfix.append(stack.pop())

    return postfix


def calculate(postfix):
    stack = []

    for unit in postfix:
        if unit in TYPES:
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(CALCULATION[unit](number1, number2))
        else:
            stack.append(int(unit))

    return stack[0]


def solution(expression):
    operators = [s for s in expression if s in TYPES]
    numbers = re.split(f"[{TYPES}]", expression)
    result = 0

    for case in permutations(TYPES, 3):
        priority = {operator: i for i, operator in enumerate(case)}
        postfix = to_postfix(numbers, operators, priority)
        result = max(abs(calculate(postfix)), result)

    return result
