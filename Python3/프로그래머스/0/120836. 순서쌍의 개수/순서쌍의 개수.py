def solution(n):
    answer = 0
    list_n = [i for i in range(1, n+1)]
    for x in range(1, n+1):
        if n % x == 0:
            answer += 1      
    return answer