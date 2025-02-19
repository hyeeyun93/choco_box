def solution(myString):
    answer = ''
    after = 'mnopqrstuvwxyz'
    for c in myString:
        if c not in after:
            answer += 'l'
        else:
            answer += c
    return answer