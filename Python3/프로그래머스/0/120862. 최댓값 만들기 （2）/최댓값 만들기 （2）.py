def solution(numbers):
    sorted_numbers = sorted(numbers)
    a = sorted_numbers[0] * sorted_numbers[1]
    b = sorted_numbers[-1] * sorted_numbers[-2]
    answer = max(a, b)
    return answer