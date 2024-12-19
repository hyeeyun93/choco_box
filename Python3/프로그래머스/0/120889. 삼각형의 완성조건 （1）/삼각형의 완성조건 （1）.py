def solution(sides):
    answer = 0
    if sum(sides) - max(sides) <= max(sides):
        answer = 2
    else:
        answer = 1
    return answer