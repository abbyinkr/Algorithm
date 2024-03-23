def solution(myString, pat):
    strs = myString.lower()
    pats = pat.lower()
    if pats in strs:
        return 1
    return 0