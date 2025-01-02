def solution(my_string):
    not_sorted = [int(i) for i in my_string if i.isdigit()]
    answer = sorted(not_sorted)
    return answer