def solution(s):
    s_list = s.split()
    c = 0
    
    while c < len(s_list):
        try:
            if s_list[c] == 'Z':
                del s_list[c-1:c+1]
                c -= 1
        except IndexError:
            pass
        c += 1
    
    answer = sum(map(int, s_list))
    
    return answer
