# 플래티넘 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
weights, happy = [], []
dp = [0] * (m + 1)

# 무게를 어떻게 쪼갤지 표를 미리 만듦
table = [[] for _ in range(10001)]
step, temp = 0, 0
for i in range(1, 10001):
    table[i] += table[i - 1]
    if temp == 0:
        table[i] = [1] + table[i]
        temp = step
        step += 1
    else:
        table[i][temp] += 1
        temp -= 1

for _ in range(n):
    v, c, k = map(int, input().split())
    n += len(table[k]) - 1
    for counts in table[k]:
        weights.append(v * counts)
        happy.append(c * counts)

for i in range(n):
    for j in range(m, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + happy[i])

print(max(dp))


# [개선된 풀이(아래)]
# k가 8이라면 이진수로 변환했을 때 1000이다. 따라서 각 자릿수마다 상품을 묶을 수 있다.
# 1개, 2개, 4개, 8개 짜리로 묶으면 1~8개의 모든 경우가 커버된다.
# 하지만 8개를 넣는경우, 1, 2, 4, 8개 모두를 선택했을 때 총량인 8보다 커지게 된다.
# 따라서 1, 2, 4개 까지 뽑는 과정에서 k를 해당 개수만큼 줄여나가다가, 개수보다 작아지면 남은 개수만큼만 묶어준다.
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
weights, happy = [], []
dp = [0] * (m + 1)

for _ in range(n):
    v, c, k = map(int, input().split())
    n -= 1  # 묶음을 추가로 넣기 위한 갯수 보정1
    counts = 1

    while k > 0:
        bundle = min(counts, k)  # 묶음 개수가 너무 커지면 남은 k만큼을 묶음 개수로 넣는다.
        weights.append(v * bundle)
        happy.append(c * bundle)
        k -= counts
        counts *= 2  # 이진 자리수 만큼 넣기 위해 2를 곱한다.
        n += 1  # 묶음을 추가로 넣기 위한 갯수 보정2

for i in range(n):
    for j in range(m, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + happy[i])

print(max(dp))
