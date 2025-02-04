def solution(num, total):
    answer = []
    if total != 0:
        mid = total // num
    else:
        mid = 0
    
    if total % num == 0:
        answer = [a for a in range(mid-(num//2), mid+(num//2)+1)]
    elif total % num != 0:
        answer = [b for b in range(mid-(num//2)+1, mid+(num//2)+1)]
    elif num == 1:
        answer.append(total)
    return answer