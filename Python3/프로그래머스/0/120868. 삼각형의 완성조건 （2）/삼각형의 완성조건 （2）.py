def solution(sides):
    answer = 0
    
    for n in range(1, sum(sides)):
        if n + sides[0] > max(sides) and n + sides[1] > max(sides):
            answer += 1
            
    return answer