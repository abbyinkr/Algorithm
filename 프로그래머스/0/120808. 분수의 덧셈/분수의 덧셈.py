import math

def solution(numer1, denom1, numer2, denom2):
    num = (numer2 * denom1) + (numer1 * denom2)
    denom = denom1 * denom2
    g = math.gcd(num, denom)
    return [num//g, denom//g]