def solution(str1, str2):
    
    answer = ''
    
    '''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    '''
    
    # zip 함수 사용하여 풀기
    for s1, s2 in zip(str1, str2):
        answer += s1+s2
    
    return answer