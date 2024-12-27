def solution(n):
    answer = 0
    sqr = n ** 0.5
    if n % sqr == 0:
        answer = 1
    else:
        answer = 2
    return answer