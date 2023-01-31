# 완전탐색 (https://school.programmers.co.kr/learn/courses/30/lessons/84512)

def solution(word):
    vowel = {"A": "E", "E": "I", "I": "O", "O": "U"}
    now_word = ["A"]
    counts = 1

    while word != "".join(now_word):
        if len(now_word) < 5:
            now_word.append("A")
        else:
            while now_word[-1] == "U":
                now_word.pop()
            now_word[-1] = vowel[now_word[-1]]

        counts += 1

    return counts
