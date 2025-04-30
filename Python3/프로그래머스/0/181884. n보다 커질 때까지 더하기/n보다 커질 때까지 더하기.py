def solution(numbers, n):
    answer = 0
    for d in numbers:
        answer += d
        if answer > n:
            break
    return answer