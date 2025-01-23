def solution(a, b):
    answer = 0
    for n in range(min(a, b), max(a, b)+1):
        answer += n
        if a == b:
            return a
    return answer