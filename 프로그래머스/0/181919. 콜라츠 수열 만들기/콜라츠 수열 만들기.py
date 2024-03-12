def solution(n):
    answer = []
    while n:
        answer.append(n)
        if n == 1:
            break
        x = 3 * n + 1 if n % 2 else n // 2
        n = x
    return answer