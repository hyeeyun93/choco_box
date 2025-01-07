def solution(my_str, n):
    answer = []
    for c in range(0, len(my_str), n):
        splitted = my_str[c:c+n]
        answer.append(splitted)
    return answer