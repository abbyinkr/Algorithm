def solution(num_list):
    a = 1
    sum = 0
    for num in num_list:
        a *= num
        sum += num
        
    if a < sum ** 2:
        return 1
    if a > sum ** 2:
        return 0
    