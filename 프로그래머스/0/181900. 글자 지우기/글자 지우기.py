def solution(my_string, indices):
    
#     strings = list(my_string)
    
#     for idx in indices:
#         strings[idx] = ''
        
#     return ''.join(strings)

    return ''.join([value for idx, value in enumerate(my_string) if idx not in indices])
    
    