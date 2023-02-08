# https://school.programmers.co.kr/learn/courses/15007/lessons/121681

# 1. 다중 분기 풀이
def solution(serial):
    answer = ""

    gender = serial[:2]
    department = serial[2:4]
    team = int(serial[4:6])
    valid_number = int(serial[6:])

    # 1. 성별
    if gender == "01":
        answer += "male"
    else:
        answer += "female"

    answer += "/"

    # 2. 소속 부서
    if department == "10":
        answer += "operation"
    elif department == "11":
        answer += "sales"
    elif department == "12":
        answer += "develop"
    elif department == "13":
        answer += "finance"
    elif department == "14":
        answer += "law"
    else:
        answer += "research"

    answer += "/"

    # 3. 소속 팀
    answer += f"{team}team/"

    # 4. 유효성 번호
    total = 0
    for number in serial[:6]:
        total += int(number)

    if total % 13 == valid_number:
        answer += "valid"
    else:
        answer += "invalid"

    return answer


# 2. 리스트를 이용한 풀이
def solution(serial):
    answer = ""
    genders = ["male", "female"]
    departments = ["operation", "sales", "develop", "finance", "law", "research"]

    gender = int(serial[1])
    department = int(serial[3])
    team = int(serial[4:6])
    valid_number = int(serial[6:])

    # 1. 성별
    answer += genders[gender - 1] + "/"

    # 2. 소속 부서
    answer += departments[department] + "/"

    # 3. 소속 팀
    answer += f"{team}team/"

    # 4. 유효성 번호
    total = gender + 1 + department + (team // 10) + (team % 10)

    if total % 13 == valid_number:
        answer += "valid"
    else:
        answer += "invalid"

    return answer


# 3. 딕셔너리를 이용한 풀이
def solution(serial):
    answer = ""
    information = {
        "01": "male",
        "02": "female",
        "10": "operation",
        "11": "sales",
        "12": "develop",
        "13": "finance",
        "14": "law",
        "15": "research"
    }

    gender = serial[:2]
    department = serial[2:4]
    team = int(serial[4:6])
    valid_number = int(serial[6:])

    # 1. 성별
    answer += information[gender] + "/"

    # 2. 소속 부서
    answer += information[department] + "/"

    # 3. 소속 팀
    answer += f"{team}team/"

    # 4. 유효성 번호
    total = 0
    for number in serial[:6]:
        total += int(number)

    if total % 13 == valid_number:
        answer += "valid"
    else:
        answer += "invalid"

    return answer
