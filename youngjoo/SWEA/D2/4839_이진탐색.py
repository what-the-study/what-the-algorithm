# Binary search

def binary_search(number):
    l, r = 1, p
    counts = 0

    while l < r:
        c = (l + r) // 2
        counts += 1

        if c == number:
            return counts

        if c < number:
            l = c
        else:
            r = c


for t in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())
    a_counts = binary_search(a)
    b_counts = binary_search(b)

    print(f"#{t}", end=" ")
    if a_counts < b_counts:
        print("A")
    elif a_counts == b_counts:
        print(0)
    else:
        print("B")
