# https://school.programmers.co.kr/learn/courses/15006/lessons/121418

def solution(num_list):
    answer = []

    for num in num_list:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        answer.append(is_prime)

    return answer
