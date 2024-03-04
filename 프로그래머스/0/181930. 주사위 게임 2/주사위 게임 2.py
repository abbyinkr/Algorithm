def solution(a, b, c):
    check = len({a, b, c})
    if check == 1:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2 ) * (a ** 3 + b ** 3 + c ** 3)
    if check == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2 )
    if check == 3:
        return a + b + c
    
    # if a != b and a != c and b != c:
    #     return a + b + c
    # elif a != b or b != c or a != c:
    #     return (a + b + c) * (a ** 2 + b ** 2 + c ** 2 )
    # elif a == b == c:
    #     return (a + b + c) * (a ** 2 + b ** 2 + c ** 2 ) * (a ** 3 + b ** 3 + c ** 3)
    