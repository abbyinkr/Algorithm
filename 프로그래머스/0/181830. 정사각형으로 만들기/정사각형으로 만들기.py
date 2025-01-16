def solution(arr):
    r = len(arr)
    c = len(arr[0]) if r > 0 else 0
    
    if r > c:
        for i in range(r):
            arr[i].extend([0] * (r - c))
            #arr[i].append(0)
    elif r < c:
        for i in range(c-r):
            arr.append([0] * c)  # 행 추가
            #arr.append([0 for _ in range(c)])
    return arr