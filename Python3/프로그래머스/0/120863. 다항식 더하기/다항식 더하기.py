def solution(polynomial):
    num = [c.strip() for c in polynomial.split('+')]
    xnum = 0
    constant = 0
    
    for i in num:
        if 'x' in i:
            if i == 'x':
                xnum += 1
            else:
                xnum += int(i.strip('x'))            
        else:
            constant += int(i)
    
    if xnum == 0:
        if constant == 0:
            answer = '0'
        else:
            answer = str(constant)
    elif xnum != 0 and constant == 0:
        if xnum == 1:
            answer = 'x'
        else:
            answer = f'{xnum}x'
    elif xnum != 0 and constant != 0:
        if xnum == 1:
            answer = f'x + {constant}'
        else:
            answer = f'{xnum}x + {constant}'
    return answer
            