def solution(n):
    answer = 0
    if 0 < n % 7 < 7:
        answer = (n // 7) + 1
    elif n % 7 == 0:
        answer = n // 7
    return answer

# n  // %
# 07 1  0  1
# 01 0  1  1
# 15 2  1  3
# 20 2  6  3
# 