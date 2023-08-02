# 이진 변환 반복하기

def solution(s):
    counts = zeros = 0

    while s != "1":
        counts += 1
        next_s = s.replace("0", "")
        zeros += len(s) - len(next_s)
        s = format(len(next_s), "b")

    return [counts, zeros]
