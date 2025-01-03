def solution(emergency):
    answer = []
    srt_list = sorted(emergency, reverse = True)    # 76,24,3
    count = len(srt_list)
    while count > 0:
        for i in emergency:
            for j in srt_list:
                if i == j:
                    answer.append(srt_list.index(j)+1)
                    count -= 1
    return answer