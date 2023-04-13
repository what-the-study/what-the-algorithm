# 브론즈 1

def fib_recursion(n):
    if n == 1 or n == 2:
        global result1
        result1 += 1
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_dp(n):
    global result2
    memo = [0, 1, 1]
    for i in range(3, n + 1):
        result2 += 1
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]


n = int(input())
result1, result2 = 0, 0
fib_recursion(n)
fib_dp(n)

print(result1, result2)
