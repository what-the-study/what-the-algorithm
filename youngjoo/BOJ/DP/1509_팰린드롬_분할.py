# 골드 1

word = input()
n = len(word)
is_palindrome = [[False] * n for _ in range(n)]
dp = [i for i in range(n + 1)]

for i in range(n):
    is_palindrome[i][i] = True

for i in range(1, n):
    for j in range(n - i):
        s, e = j, i + j
        if word[s] == word[e] and (i == 1 or is_palindrome[s + 1][e - 1]):
            is_palindrome[s][e] = True
        else:
            is_palindrome[s][e] = False

for e in range(n):
    for s in range(e + 1):
        if is_palindrome[s][e]:
            dp[e + 1] = min(dp[e + 1], dp[s] + 1)

print(dp[-1])
