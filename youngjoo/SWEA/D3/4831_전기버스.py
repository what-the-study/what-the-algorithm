# List

for t in range(1, int(input()) + 1):
    k, n, m = map(int, input().split())
    chargers = set(map(int, input().split()))
    bus = k
    result = 0

    while bus < n:
        for i in range(k):
            temp = bus - i
            if temp in chargers:
                result += 1
                bus = temp
                break
        else:
            result = 0
            break

        bus += k

    print(f"#{t} {result}")
