def solution(s1, s2):
    answer = len([t for t in s1 if t in s2])
    return answer