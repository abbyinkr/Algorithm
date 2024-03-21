def solution(arr):
    answer = []
    for num in arr:
        if 50 <= num and num % 2 == 0:
            num = num//2
        elif num < 50 and num % 2 == 1:
            num *= 2
        answer.append(num)
    return answer