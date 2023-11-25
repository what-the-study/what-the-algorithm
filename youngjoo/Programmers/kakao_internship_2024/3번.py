# 3. 주사위 굴리기

from itertools import combinations


from itertools import combinations


def solution(dice):
    def get_all_dice_number(depth, total, case, result):
        if depth == len(dice) // 2:
            result.append(total)
            return

        for i in range(6):
            get_all_dice_number(depth + 1, total + dice[case[depth]][i], case, result)

    dice_numbers = list(range(len(dice)))
    max_wins = 0

    for a_case in combinations(dice_numbers, len(dice) // 2):
        b_case = [number for number in dice_numbers if number not in a_case]
        a_result = []
        b_result = []

        get_all_dice_number(0, 0, a_case, a_result)
        get_all_dice_number(0, 0, b_case, b_result)

        wins = 0
        a_result.sort()
        b_result.sort()

        for i in a_result:
            for j in b_result:
                if i <= j:
                    break
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
