def solution(quiz):
    answer = []
    changed = [i.split() for i in quiz]
    check = []
    for a in changed:
        if '-' in a:
            check.append(int(a[0]) - int(a[2]))
        else:
            check.append(int(a[0]) + int(a[2]))
    for c in range(len(check)):
        if int(changed[c][4]) == check[c]:
            answer.append('O')
        else:
            answer.append('X')
    return answer
                