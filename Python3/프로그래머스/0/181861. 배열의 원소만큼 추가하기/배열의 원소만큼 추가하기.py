def solution(arr):
    answer = []
    for n in arr:
        for  _ in range(int(n)):
            answer.append(int(n))
    return answer