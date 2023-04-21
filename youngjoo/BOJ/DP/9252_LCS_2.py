# 골드 4

def lcs(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    check = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                check[i][j] = 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                check[i][j] = 2 if dp[i][j - 1] > dp[i - 1][j] else 3

    i, j = len(s1), len(s2)
    result = []

    while i > 0 and j > 0:
        if check[i][j] == 1:
            result.append(s1[i - 1])

        dx, dy = dxy[check[i][j]]
        i += dx
        j += dy

    return dp[-1][-1], "".join(result[::-1])


dxy = [0, (-1, -1), (0, -1), (-1, 0)]
print(*lcs(input(), input()), sep="\n")
