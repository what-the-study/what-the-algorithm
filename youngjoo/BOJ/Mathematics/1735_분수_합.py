# 실버 3

from fractions import Fraction

a = Fraction(*map(int, input().split()))
b = Fraction(*map(int, input().split()))
result = a + b
print(result.numerator, result.denominator)
