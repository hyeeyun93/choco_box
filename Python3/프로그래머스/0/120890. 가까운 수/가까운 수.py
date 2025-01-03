def solution(array, n):
    sorted_array = sorted(array)
    abs_list = [abs(x - n) for x in sorted_array]
    
    answer = sorted_array[abs_list.index(min(abs_list))]
    
    return answer