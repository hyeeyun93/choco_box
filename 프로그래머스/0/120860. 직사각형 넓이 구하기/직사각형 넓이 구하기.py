def solution(dots):

    for i in range(4):
        for j in range(i+1, 4):
            a = dots[i]
            b = dots[j]
            if not (a[0] in b or a[1] in b):
                answer = abs(a[0] - b[0]) * abs(a[1] - b[1])
    return answer