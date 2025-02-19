def solution(num_list):
    even = num_list[1]
    odd = num_list[0]
    for i in range(2, len(num_list)):
        if i % 2 == 0:
            odd += num_list[i]
        else:
            even += num_list[i]
    return max(even, odd)