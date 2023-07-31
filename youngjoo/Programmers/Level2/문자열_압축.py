# 문자열 압축

def solution(s):
    result = len(s)

    for unit in range(1, len(s) // 2 + 1):
        i, j = 0, unit
        counts, zipped = 1, ""

        while i < len(s):
            if s[i:j] == s[i + unit:j + unit]:
                counts += 1
            else:
                temp = s[i:j] if counts == 1 else f"{counts}{s[i:j]}"
                zipped += temp
                counts = 1

            i += unit
            j += unit

        result = min(len(zipped), result)

    return result
