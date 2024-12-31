def solution(num, k):
    answer = 0
    num_list = [int(n) for n in str(num)]
    if k in num_list:
        answer = num_list.index(k) + 1
    else:
        answer = -1
    return answer