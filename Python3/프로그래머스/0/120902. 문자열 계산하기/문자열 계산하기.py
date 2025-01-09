def solution(my_string):
    
    breakdown = [c for c in my_string.split() if c != ' ']
    answer = int(breakdown[0])
    
    for p in range(1, len(breakdown)-1):
        if breakdown[p] == '+':
            answer += int(breakdown[p+1])
        elif breakdown[p] == '-':
            answer -= int(breakdown[p+1])
    
    return answer