def solution(n, control):
    
    values = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum([values[c] for c in control])