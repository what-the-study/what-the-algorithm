# 튜플

def solution(s):
    elements = list(map(lambda x: set(x.split(",")), s.strip("{}").split("},{")))
    elements.sort(key=lambda x: len(x))
    prev, result = set(), []

    for element in elements:
        result.append(int(list(element - prev)[0]))
        prev = element

    return result
