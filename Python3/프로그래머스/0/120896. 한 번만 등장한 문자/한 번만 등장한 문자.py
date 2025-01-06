def solution(s):
    check = ''
    
    for i in s:
        if s.count(i) == 1:
            check += i
    
    answer = ''.join(sorted(check))
    
    return answer