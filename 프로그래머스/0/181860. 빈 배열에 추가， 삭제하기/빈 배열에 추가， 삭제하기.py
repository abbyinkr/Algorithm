def solution(arr, flag):
    answer = []
    for i, f in zip(arr, flag):
        if f is True:
            for _ in range(i * 2):
                answer.append(i)
        else:
            for _ in range(i):
                answer.pop()    
    return answer