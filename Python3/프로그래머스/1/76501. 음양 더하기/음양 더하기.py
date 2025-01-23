def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] = -(absolutes[i])
    return sum(absolutes)