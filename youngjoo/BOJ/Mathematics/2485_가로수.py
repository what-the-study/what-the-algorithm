# 실버 4

import sys, math

input = sys.stdin.readline

n = int(input())
tree = [int(input()) for _ in range(n)]
diff = [tree[i] - tree[i - 1] for i in range(1, n)]
standard = math.gcd(*diff)
print(sum(d // standard - 1 for d in diff))
