def solution(arr):
    length = len(arr)
    while (length & (length - 1)) != 0:
        arr.append(0)
        length += 1
    return arr
    