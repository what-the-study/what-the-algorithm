# Basic Python

factors = [2, 3, 5, 7, 11]

for t in range(1, int(input()) + 1):
    n = int(input())
    result = []

    for factor in factors:
        counts = 0
        while n % factor == 0:
            n //= factor
            counts += 1
        result.append(counts)

    print(f"#{t}", *result)
