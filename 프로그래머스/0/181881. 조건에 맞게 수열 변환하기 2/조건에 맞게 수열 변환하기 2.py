def solution(arr):
    x = 0
    while(True):
        array = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                array.append(i//2)
            elif i < 50 and i % 2 == 1:
                array.append(i*2+1)
            else:
                array.append(i)
        if array == arr:
            break
        x += 1
        arr = array        
    return x