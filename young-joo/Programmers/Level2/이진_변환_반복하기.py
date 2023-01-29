# 월간 코드 챌린지 시즌1 (https://school.programmers.co.kr/learn/courses/30/lessons/70129)

def solution(s):
    zero_deletes, binary_counts = 0, 0

    while s != "1":
        zero = s.count("0")
        zero_deletes += zero
        s = format(len(s) - zero, "b")
        binary_counts += 1

    return [binary_counts, zero_deletes]
