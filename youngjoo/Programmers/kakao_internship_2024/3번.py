# 3. 주사위 굴리기

from itertools import combinations


def solution(dice):
    def recursion(depth, total, case, result):
        if depth == len(dice) // 2:
            result.append(total)
            return total

        for i in range(6):
            recursion(depth + 1, total + dice[case[depth]][i], case, result)

    dice_numbers = list(range(len(dice)))
    a_cases = list(combinations(dice_numbers, len(dice) // 2))
    max_wins = 0

    for a_case in a_cases:
        b_case = [number for number in dice_numbers if number not in a_case]
        a_result = []
        b_result = []

        recursion(0, 0, a_case, a_result)
        recursion(0, 0, b_case, b_result)

        wins = 0

        for i in a_result:
            for j in b_result:
                if i > j:
                    wins += 1

        if max_wins < wins:
            max_wins = wins
            answer = [i + 1 for i in a_case]

    return answer


print(
    solution(
        [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
    )
)
