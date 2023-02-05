# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) (https://school.programmers.co.kr/learn/courses/30/lessons/77484)

def solution(lottos, win_nums):
    lotto_count, zero_count = 0, 0

    for number in lottos:
        if number in win_nums:
            lotto_count += 1
        elif number == 0:
            zero_count += 1

    max_order = 7 - (lotto_count + zero_count)
    min_order = 7 - lotto_count

    if max_order == 7:
        max_order = 6
    if min_order == 7:
        min_order = 6

    return [max_order, min_order]
