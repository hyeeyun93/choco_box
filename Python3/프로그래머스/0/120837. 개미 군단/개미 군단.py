def solution(hp):
    answer = 0
    while hp >= 0:
        if 5 <= hp:
            answer += 1
            hp -= 5
        elif 3 <= hp < 5:
            answer += 1
            hp -= 3
        elif hp < 3:
            answer += 1
            hp -= 1
    return answer - 1