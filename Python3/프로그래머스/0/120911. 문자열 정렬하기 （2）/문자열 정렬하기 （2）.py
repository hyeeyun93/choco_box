def solution(my_string):
    not_sorted = [c for c in my_string.lower()]
    yes_sorted = sorted(not_sorted)
    answer = ''
    for c in yes_sorted:
        answer += c
    return answer