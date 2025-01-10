def solution(picture, k):
    answer = []
    for pic in picture:
        str = ""
        for p in pic:
            str += p * k
        for _ in range(k):
            answer.append(str)
    return answer
    
