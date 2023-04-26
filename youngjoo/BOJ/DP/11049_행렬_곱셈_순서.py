# 골드 3

import sys

input = sys.stdin.readline
INF = 2 ** 31

n = int(input())
sizes = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

# width => 행렬 구간 사이즈
# start => 구간의 시작 행렬 번호 (j ~ i+j 까지의 행렬 구간 형성)
# k => 모든 경우를 탐색하기 위해 결합법칙을 끊는 기준 (start ~ end)

for width in range(1, n):
    for start in range(n - width):
        end = start + width
        for k in range(start, end):
            c = dp[start][k] + dp[k + 1][end] + (sizes[start][0] * sizes[k][1] * sizes[end][1])
            dp[start][end] = min(dp[start][end], c)

print(dp[0][-1])
