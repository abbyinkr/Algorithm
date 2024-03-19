def solution(my_string):
    
    alpha_list = [i for i in range(ord('A'), ord('Z') + 1)]  # 대문자 A~Z
    alpha_list += [i for i in range(ord('a'), ord('z') + 1)]  # 소문자 a~z
    alpha_dict = {ord: 0 for ord in alpha_list}
    ord_list = [ord(char) for char in my_string]
    
    for ord_char in ord_list:
        alpha_dict[ord_char] += 1
        
    return list(alpha_dict.values())
        