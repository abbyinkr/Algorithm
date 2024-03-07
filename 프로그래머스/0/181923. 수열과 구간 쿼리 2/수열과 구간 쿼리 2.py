def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = []
        flag = False
        for i in range(s, e+1):
            if k < arr[i]:
                temp.append(arr[i])
                flag = True
        if flag is True:
            answer.append(min(temp))
        else:
            answer.append(-1)
    return answer