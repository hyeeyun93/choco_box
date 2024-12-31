def solution(order):
    answer = 0
    order_list = [int(c) for c in str(order)]
    check_list = [3, 6, 9]
    for num in order_list:
        if num in check_list:
            answer += 1
    return answer