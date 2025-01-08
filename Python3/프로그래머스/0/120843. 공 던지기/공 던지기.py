def solution(numbers, k):
    thrown = 2 * (k-1)
    
    if thrown >= len(numbers):
        return numbers[thrown % len(numbers)]
    else:
        return numbers[thrown]