# https://school.programmers.co.kr/learn/courses/15007/lessons/121676

n = int(input())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)
