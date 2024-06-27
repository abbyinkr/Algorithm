
def solution(myStr):
    result = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return [s for s in result if s] if result else ["EMPTY"]
    

    
    