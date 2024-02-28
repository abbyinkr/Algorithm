def solution(ineq, eq, n, m):
    tuple = (ineq, eq)
    if n <= m and tuple == ("<", "="):
        return 1
    if n >= m and tuple == (">", "="):
        return 1
    if n < m and tuple == ("<", "!"):
        return 1
    if n > m and tuple == (">", "!"):
        return 1
    return 0