def solution(my_string, is_prefix):
    if is_prefix in [my_string[:i] for i in range(len(my_string))]:
        return 1
    return 0