# https://school.programmers.co.kr/learn/courses/15006/lessons/121350

num_list = [1, 3, 5, 2, 12]

for i in range(len(num_list)):
    for j in range(num_list[i]):
        print(num_list[i], end=' ')
    print()
