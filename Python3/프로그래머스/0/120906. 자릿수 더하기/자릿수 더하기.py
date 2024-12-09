def solution(n):
    n_string = str(n)
    answer = 0
    for i in n_string:
        answer += int(i)
    return answer