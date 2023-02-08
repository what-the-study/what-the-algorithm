# https://school.programmers.co.kr/learn/courses/15006/lessons/121431

def solution(text, anagram, sw):
    answer = [""] * len(text)

    if sw:
        # 암호화
        for i in range(len(anagram)):
            answer[anagram[i]] = text[i]
    else:
        # 복호화
        for i in range(len(anagram)):
            answer[i] = text[anagram[i]]

    return "".join(answer)
