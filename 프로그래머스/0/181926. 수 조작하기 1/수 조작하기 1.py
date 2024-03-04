def solution(n, control):
    
    for c in control:
        if c == "w":
            n += 1
            continue
        elif c == "s":
            n -= 1
            continue
        elif c == "d":
            n += 10
            continue
        elif c == "a":
            n -= 10
            continue
    return n