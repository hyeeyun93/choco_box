def solution(dots):
    n = len(dots)
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            dx1 = x2 - x1
            dy1 = y2 - y1
            
            for k in range(n):
                for l in range(k+1, n):
                    if i in (k, l) or j in (k, l):
                        continue
                    x3, y3 = dots[k]
                    x4, y4 = dots[l]
                    dx2 = x4 - x3
                    dy2 = y4 - y3
                    
                    if dy1 * dx2 == dy2 * dx1:
                        return 1
    return 0