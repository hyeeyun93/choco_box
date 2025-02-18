def solution(str_list, ex):
    answer = ''
    for w in str_list:
        if ex not in w:
            answer += w
    return answer