def solution(n):
# 최소공배수 구하기
    a =  6 * n // gcd(6, n)
    return a // 6
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)