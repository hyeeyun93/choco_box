def solution(myString):
    answer = []
    cut = myString.split('x')
    for c in cut:
        answer.append(len(c))
    return answer