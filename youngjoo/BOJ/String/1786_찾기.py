# 플래티넘 5

import sys

input = sys.stdin.readline


# 접두사, 접미사 동일 배열 만들기
def make_table(pattern):
    table = [0]
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]

        if pattern[i] == pattern[j]:
            i += 1

        table.append(i)

    return table


# parent에서 pattern을 찾는 kmp 알고리즘
def kmp(parent, pattern):
    index = []
    table = make_table(pattern)
    j = 0

    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                index.append(i - len(pattern) + 2)  # 위치가 1부터 시작이므로 +2를 했음
                j = table[j]
            else:
                j += 1

    return index


sentence = input().rstrip()
word = input().rstrip()

result = kmp(sentence, word)

print(len(result))  # 발견된 개수
print(*result)  # 발견된 위치 목록
