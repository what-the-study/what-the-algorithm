# 실버 2

n = int(input())
numbers = list(map(int, input().split()))
numbers_set = sorted(set(numbers))
numbers_dict = {number: i for i, number in enumerate(numbers_set)}

for number in numbers:
    print(numbers_dict[number], end=" ")
