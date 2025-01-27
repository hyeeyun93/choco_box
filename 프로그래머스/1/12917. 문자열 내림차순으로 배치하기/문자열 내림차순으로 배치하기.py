def solution(s):
    upper = [c for c in sorted(s, reverse=True) if c.isupper()]
    lower = [d for d in sorted(s, reverse=True) if d.islower()]
    answer = ''.join(lower + upper)
    return answer