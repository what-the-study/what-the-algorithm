# 실버 4

input()
a = set(input().split())
b = set(input().split())
print(len((a | b) - (a & b)))
