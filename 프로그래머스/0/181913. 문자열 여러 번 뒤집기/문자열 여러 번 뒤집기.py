def solution(my_string, queries):
    chars = [char for char in my_string]
    for s, e in queries:
        for i in range(s, e+1):
            if i > s+e-i:
                break
            a = chars[i]
            b = chars[s+e-i]
            chars[i] = b
            chars[s+e-i] = a
    return ''.join(chars)