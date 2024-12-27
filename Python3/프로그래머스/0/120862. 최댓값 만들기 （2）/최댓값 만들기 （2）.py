def solution(numbers):
    multi = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                multi.append(numbers[i] * numbers[j])
    answer = max(multi)
    return answer