def solution(n):
    answer = 0
    if 0 < n % 7 < 7:
        answer = (n // 7) + 1
    elif n % 7 == 0:
        answer = n // 7
    return answer