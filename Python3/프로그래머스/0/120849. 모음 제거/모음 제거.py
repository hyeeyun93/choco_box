def solution(my_string):
    answer = ''
    my_string_list = list(my_string)
    for i in my_string_list:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            answer += i
    return answer