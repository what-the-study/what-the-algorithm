# 골드 2

def multiply(m1, m2):
    return [[sum(m1[i][k] * m2[k][j] for k in range(2)) % BIG for j in range(2)] for i in range(2)]


def fibo(n, matrix):
    if n == 1:
        return matrix

    if n % 2 == 0:
        temp = fibo(n // 2, matrix)
        return multiply(temp, temp)

    return multiply(fibo(n - 1, matrix), matrix)


n = int(input())
BIG = 1_000_000_007
print(n if n <= 1 else fibo(n - 1, [[1, 1], [1, 0]])[0][0])
