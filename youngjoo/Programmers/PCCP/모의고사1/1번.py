from collections import Counter, defaultdict


def solution(input_string):
    original_counter = Counter(input_string)
    counter = defaultdict(int)
    alone = set()

    for i in range(len(input_string) - 1):
        char1, char2 = input_string[i], input_string[i + 1]

        if char1 in alone:
            continue

        counter[char1] += 1

        if char1 == char2:
            continue

        if counter[char1] < original_counter[char1]:
            alone.add(char1)

    return "".join(sorted(alone)) if alone else "N"