def solution(bin1, bin2):
    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    
    answer = bin(dec1 + dec2)
    return answer[2:]