def solution(my_string, m, c):
    # strings = [my_string[i:i+m] for i in range(len(my_string)) if i % m == 0]
    # return ''.join([string[c-1] for string in strings])
    return my_string[c-1::m]