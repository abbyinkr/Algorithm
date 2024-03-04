def solution(code):
    mode = 0
    ret = ""
    for idx in range(0, len(code)):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            if code[idx] == "1":
                mode = 1
        elif mode == 1:
            if code[idx] != "1" and idx % 2 == 1:
                ret += code[idx]
            if code[idx] == "1":
                mode = 0
    
    return "EMPTY" if len(ret)==0 else ret 