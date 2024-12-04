def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i / len(numbers)            
    return answer