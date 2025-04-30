def solution(n, control):
    
    for e in control:
        if e == "w":
            n += 1
        elif e == "s":
            n -= 1
        elif e == "d":
            n += 10
        else:
            n -= 10
    return n