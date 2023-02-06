#

for t in range(1, int(input()) + 1):
    d, a, b, f = map(int, input().split())
    print(f"#{t} {(d / (a + b)) * f}")
