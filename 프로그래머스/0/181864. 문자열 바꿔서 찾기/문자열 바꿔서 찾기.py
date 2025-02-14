def solution(myString, pat):
    answer = 0
    swapped = ''
    for c in myString:
        if c == 'A':
            swapped += 'B'
        else:
            swapped += 'A'
    
    if pat in swapped:
        answer = 1
    else:
        answer = 0
    return answer