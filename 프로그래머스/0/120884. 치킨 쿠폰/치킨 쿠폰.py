def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        extra = coupon // 10
        answer += extra
        coupon = coupon % 10 + extra
        
    return answer