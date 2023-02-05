# List

from collections import Counter

for t in range(1, int(input()) + 1):
    _ = input()
    counter = Counter(sorted(map(int, input()), reverse=True)).most_common()
    print(f"#{t}", *counter[0])
