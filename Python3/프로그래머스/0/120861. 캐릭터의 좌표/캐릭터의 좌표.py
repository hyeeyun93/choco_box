def solution(keyinput, board):
    answer = [0, 0]
    x_max = board[0] // 2
    y_max = board[1] // 2
    
    for k in keyinput:
        if k == 'up':
            answer[1] += 1
            if abs(answer[1]) > y_max:
                answer[1] = y_max
        elif k == 'down':
            answer[1] -= 1
            if abs(answer[1]) > y_max:
                answer[1] = -(y_max)
        elif k == 'left':
            answer[0] -= 1
            if abs(answer[0]) > x_max:
                answer[0] = -(x_max)
        elif k == 'right':
            answer[0] += 1
            if abs(answer[0]) > x_max:
                answer[0] = x_max
    
    return answer