def solution(numbers):
    max_index = numbers.index(max(numbers))
    max_num = numbers.pop(max_index)
    answer = max_num * max(numbers)
    return answer