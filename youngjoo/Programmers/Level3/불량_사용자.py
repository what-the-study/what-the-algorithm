# 불량 사용자

from itertools import permutations


def is_matched(user, banned):
    if len(user) != len(banned):
        return False

    for i in range(len(user)):
        if banned[i] != "*" and banned[i] != user[i]:
            return False

    return True


def solution(user_id, banned_id):
    result = set()

    for case in permutations(user_id, len(banned_id)):
        temp = []

        for banned in banned_id:
            for user in case:
                if user not in temp and is_matched(user, banned):
                    temp.append(user)
                    break

        if len(banned_id) == len(temp):
            result.add("".join(sorted(temp)))

    return len(result)
