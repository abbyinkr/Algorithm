def solution(str_list):
    s = ''.join(str_list)
    for c in s:
        if c == "l":
            return str_list[:s.index("l")]
        if c == "r":
            return str_list[s.index("r")+1:]
    return []