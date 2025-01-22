def solution(A, B):
    answer = 0
    A_list = [a for a in A]
    B_list = [b for b in B]
    
    if A == B:
        return answer
    
    for _ in range(len(A)):
        A_list = A_list[-1:] + A_list[:-1]
        answer += 1
        if A_list == B_list:
            return answer
    return -1