# 소수 찾기

from itertools import permutations


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    result = set()

    for i in range(1, len(numbers) + 1):
        for case in permutations(numbers, i):
            number = int("".join(case))

            if number >= 2 and is_prime(number):
                result.add(number)

    return len(result)
