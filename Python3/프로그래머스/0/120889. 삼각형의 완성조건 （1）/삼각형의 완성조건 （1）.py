def solution(sides):
    answer = 0
    if sum(sides) - (max(sides) * 2) <= 0:
        answer = 2
    else:
        answer = 1
    return answer