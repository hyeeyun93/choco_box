import time

start = time.time()

def solution(board):
    size = len(board[0])
    answer = size * size
    bomb = set()
    
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                for i in range(max(0, x-1), min(size, x+2)):
                    for j in range(max(0, y-1), min(size, y+2)):
                        bomb.add((i, j))
                        
    return answer - len(bomb)

end = time.time()
print(end-start)