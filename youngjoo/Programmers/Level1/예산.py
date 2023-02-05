# Summer/Winter Coding(~2018) (https://school.programmers.co.kr/learn/courses/30/lessons/12982)

def solution(d, budget):
    d.sort()

    for i in range(len(d), 0, -1):
        if sum(d[:i]) <= budget:
            return i

    return 0
