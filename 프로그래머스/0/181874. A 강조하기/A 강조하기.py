def solution(myString):
    arr = []
    for c in myString:
        if c == "a":
            arr.append("A")
        elif c != "A" and c.isupper():
            arr.append(c.lower())
        else:
            arr.append(c)
    return ''.join(arr)