def solution(order):
    sum = 0
    for drink in order:
        if "americano" in drink or "anything" == drink:
            sum += 4500
            continue
        if "cafelatte" in drink:
            sum += 5000
            continue
    return sum
        
