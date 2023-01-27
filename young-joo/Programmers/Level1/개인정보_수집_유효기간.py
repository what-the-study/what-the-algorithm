# 2023 KAKAO BLIND RECRUITMENT (https://school.programmers.co.kr/learn/courses/30/lessons/150370)

def solution(today, terms, privacies):
    t_year, t_month, t_day = map(int, today.split("."))
    terms_dict = {}
    result = []

    for term in terms:
        kind, period = term.split()
        terms_dict[kind] = int(period)

    for i, privacy in enumerate(privacies):
        collecting_date, kind = privacy.split()
        year, month, day = map(int, collecting_date.split("."))

        month += terms_dict[kind]
        day -= 1

        if month > 12:
            year += month // 12
            month %= 12
            if month == 0:
                month = 12
                year -= 1

        if day < 1:
            day = 28
            month -= 1
            if month < 1:
                month = 12
                year -= 1

        if year < t_year or (year == t_year and month < t_month) or (
                year == t_year and month == t_month and day < t_day):
            result.append(i + 1)

    return result
