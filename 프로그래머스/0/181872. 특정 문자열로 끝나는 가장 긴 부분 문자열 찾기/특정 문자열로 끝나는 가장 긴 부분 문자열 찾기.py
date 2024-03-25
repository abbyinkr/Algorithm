def solution(myString, pat):
    return ''.join(myString.rpartition(pat)[:2])