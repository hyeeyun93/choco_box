def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    return [-1] if len(answer) == 0 else answer