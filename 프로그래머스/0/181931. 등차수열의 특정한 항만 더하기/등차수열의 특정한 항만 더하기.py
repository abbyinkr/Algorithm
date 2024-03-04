def solution(a, d, included):
    n = len(included)
    seq = [a + d * i for i in range(n)]
    sum = 0
    for i in range(0, n):
        if included[i] == True:
            sum += seq[i]
        
    return sum