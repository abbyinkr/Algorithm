def solution(arr):
    r = len(arr)
    c = len(arr[0]) if r > 0 else 0
    
    if r > c:
        for i in range(r):
            arr[i].extend([0] * (r - c))
    elif r < c:
        for i in range(c-r):
            arr.append([0] * c)
    return arr