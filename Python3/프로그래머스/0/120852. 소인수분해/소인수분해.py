def solution(n):
    check = set()
    
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                n //= i
                check.add(i)
                break
    
    answer = sorted(list(check))
    
    return answer