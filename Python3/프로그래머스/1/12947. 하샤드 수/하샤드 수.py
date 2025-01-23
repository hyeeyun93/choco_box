def solution(x):
    digit_sum = sum(int(i) for i in str(x))
    return True if x % digit_sum == 0 else False