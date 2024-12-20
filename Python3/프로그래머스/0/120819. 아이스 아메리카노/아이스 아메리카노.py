def solution(money):
    answer = []
    a, b = money // 5500, money % 5500
    answer.append(a)
    answer.append(b)
    return answer