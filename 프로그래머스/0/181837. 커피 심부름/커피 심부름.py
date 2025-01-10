def solution(order):
    sum = 0
    for drink in order:
        if "cafelatte" in drink:
            sum += 5000
            continue
        sum += 4500
    return sum
        
