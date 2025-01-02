def solution(my_string):
    answer = ''
    c_set = set()
    for c in my_string:
        if c not in c_set:
            c_set.add(c)
            answer += c
    return answer