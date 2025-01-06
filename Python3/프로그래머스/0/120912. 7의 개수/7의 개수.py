def solution(array):
    
    stringed = ''
    
    for i in array:
        stringed += str(i)
        
    answer = stringed.count('7')
    
    return answer