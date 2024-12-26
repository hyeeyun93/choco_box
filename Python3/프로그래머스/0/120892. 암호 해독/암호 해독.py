def solution(cipher, code):
    answer = ''
    for c in range(code - 1, len(cipher), code):
        answer = answer + cipher[c]
    return answer