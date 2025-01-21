def solution(n):
    answer = []
    a = 0

    while len(answer) < n:
        if a % 3 != 0:
            if '3' not in str(a):
                answer.append(a)
        a += 1

    return max(answer)