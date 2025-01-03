def solution(n):
    answer = 0
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = answer * factorial
    return answer - 1