def solution(my_string, alp):
    answer = ''
    for w in my_string:
        if w == alp:
            answer += w.upper()
        else:
            answer += w
    return answer