def solution(myString, pat):
    result = ""
    for char in myString:
        if char == 'A':
            result += 'B'
        elif char == 'B':
            result += 'A'
    if pat in result:
        return 1
    return 0