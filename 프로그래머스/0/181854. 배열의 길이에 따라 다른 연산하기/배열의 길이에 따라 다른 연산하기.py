def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 1:
                answer.append(arr[i] + n)
                continue
            answer.append(arr[i])
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i] + n)
                continue
            answer.append(arr[i])
    return answer