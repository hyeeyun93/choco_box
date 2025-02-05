import math

def solution(numer1, denom1, numer2, denom2):
    answer = [(numer1*denom2)+(numer2*denom1), denom1*denom2]
    
    answer_gcd = math.gcd(answer[0], answer[1])
    
    if answer_gcd == answer[0] * answer[1]:
        return answer
    else:
        return [answer[0]//answer_gcd, answer[1]//answer_gcd]