def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        move = numLog[i+1] - numLog[i]
        if move == 1:
            answer += 'w'
        elif move == -1:
            answer += 's'
        elif move == 10:
            answer += 'd'
        elif move == -10:
            answer += 'a'
    return answer