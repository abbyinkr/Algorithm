'''
1. 배열 값 모두 '0'으로 초기화
2. 값을 1부터 n*n으로 증가시키며 시계방향으로 회전하면서 배열에 값 채우기
시계방향: right, down, left, up
'''

def solution(n):
    if n == 1:
        return [[1]]
    
    x = y = 0
    dir = 'r'
    
    # 2차원 배열 초기화
    answer = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n*n):
        answer[x][y] = i + 1
        if dir == 'r':
            y += 1
            # 맨 끝에 도달했거나 가려는 곳에 이미 값이 있으면 방향 전환
            if y == n - 1 or answer[x][y+1] != 0:
                dir = 'd'
        elif dir == 'd':
            x += 1
            if x == n - 1 or answer[x+1][y] != 0:
                dir = 'l'
        elif dir == 'l':
            y -= 1
            if y == 0 or answer[x][y-1] != 0:
                dir = 'u'
        elif dir == 'u':
            x -= 1
            if x == 0 or answer[x-1][y] != 0:
                dir = 'r'
    return answer
    return answer