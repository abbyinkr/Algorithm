def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(length):
        answer.append(num_list[length-i-1])
    return answer