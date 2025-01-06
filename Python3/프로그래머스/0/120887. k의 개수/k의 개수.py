def solution(i, j, k):
    answer = 0
    num_string = ''
    
    for nums in range(i, j+1):
        num_string += str(nums)
        
    for i in num_string:
        if str(k) == i:
            answer += 1
    
    return answer