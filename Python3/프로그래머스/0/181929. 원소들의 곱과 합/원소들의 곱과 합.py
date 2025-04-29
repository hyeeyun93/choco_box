def solution(num_list):
    
    list_multiplied = 1
    for n in num_list:
        list_multiplied *= n
    
    list_squared = (sum(num_list)) ** 2
    
    if list_multiplied < list_squared:
        answer = 1
    else:
        answer = 0
        
    return answer