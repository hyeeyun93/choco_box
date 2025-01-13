def solution(balls, share):
    
    top = 1
    lower_1 = 1
    lower_2 = 1 
        
    for n in range(1, balls+1):
        top *= n
    
    for i in range(1, (balls - share)+1):
        lower_1 *= i
    
    for m in range(1, share+1):
    
        lower_2 *= m
    
    answer = top / (lower_1 * lower_2)
    
    return answer