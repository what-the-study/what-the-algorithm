# 브론즈 2

n = int(input())
x, y = 0, 1

for _ in range(n):
    x, y = y, x + y

print(x)


# def fibo(x):
#     if x <= 1:
#         return x
#     return fibo(x - 2) + fibo(x - 1)
#
#
# print(fibo(int(input())))
