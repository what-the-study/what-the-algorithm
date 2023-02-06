def is_stop(x):
    if a % 2 == 0:
        return x % 4 == 0
    return x % 3 == 0 and x % 10 != 0


for t in range(1, int(input()) + 1):
    n = int(input())
    result = [0] * 1001

    for _ in range(n):
        bus, a, b = map(int, input().split())
        result[a] += 1
        result[b] += 1

        if bus == 1:
            for i in range(a + 1, b):
                result[i] += 1
        elif bus == 2:
            for i in range(a + 2, b, 2):
                result[i] += 1
        else:
            for i in range(a + 1, b):
                if is_stop(i):
                    result[i] += 1

    print(f"#{t} {max(result)}")
