# https://school.programmers.co.kr/learn/courses/15007/lessons/121678

def solution(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()
