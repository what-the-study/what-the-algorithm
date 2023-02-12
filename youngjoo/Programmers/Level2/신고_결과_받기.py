# 2022 KAKAO BLIND RECRUITMENT (https://school.programmers.co.kr/learn/courses/30/lessons/92334)

def solution(id_list, report, k):
    reporting_users = {user: [] for user in id_list}  # 나를 신고한 유저들 목록
    answer = {user: 0 for user in id_list}

    for r in set(report):
        s, e = r.split()
        reporting_users[e].append(s)

    for users in reporting_users.values():
        if len(users) >= k:
            for user in users:
                answer[user] += 1

    return list(answer.values())
