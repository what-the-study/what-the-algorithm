# 시저 암호

def solution(s, n):
    uppers = [chr(i) for i in range(65, 91)]
    lowers = [chr(i) for i in range(97, 123)]
    result = ""

    for char in s:
        if char == " ":
            result += char
        else:
            temp = uppers if char.isupper() else lowers
            index = (temp.index(char) + n) % 26
            result += temp[index]

    return result
