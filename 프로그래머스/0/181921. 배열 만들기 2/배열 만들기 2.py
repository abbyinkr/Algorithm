def solution(l, r):
    answer = []
    for num in range(l, r+1):
        set_num = set(str(num))
        if not set_num - {"0", "5"}:
            answer.append(num)    
    return answer if answer else [-1]