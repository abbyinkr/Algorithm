from collections import Counter


def solution(a, b, c, d):
    # 가장 많이 등장하는 값과 그 개수를 튜플 형태로 반환
    most_common = Counter([a, b, c, d]).most_common()
    # 집합으로 중복 제거
    count = len({a, b, c, d})
    
    if count == 1:
        return 1111 * a
    if count == 2:
        if most_common[0][1] == 3:
            return (10 * most_common[0][0] + most_common[1][0]) ** 2
        elif most_common[0][1] == 2:
            return (most_common[0][0] + most_common[1][0]) * abs(most_common[0][0] - most_common[1][0])
    if count == 3:
        return most_common[1][0] * most_common[2][0]
    if count == 4:
        return min({a,b,c,d})
    
