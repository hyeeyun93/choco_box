def solution(num_list, n):
    answer = []
    for i in range(n, len(num_list)+1):
        if i % n == 0: #2,4,6,8
            answer.append(num_list[i-n:i])
    return answer