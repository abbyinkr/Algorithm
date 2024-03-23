from math import prod

def solution(num_list):
    multi = 1
    if len(num_list) >= 11:
        return sum(num_list)
    return prod(num_list)