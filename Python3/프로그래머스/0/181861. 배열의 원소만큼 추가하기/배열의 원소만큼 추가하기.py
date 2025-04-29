def solution(arr):
    answer = []
    for n in arr:
        for  _ in range(int(n)):
            answer += [int(n)]
    return answer