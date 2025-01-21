def solution(score):
    avg_score = [sum(s) / 2 for s in score]
    sorted_avg = sorted(avg_score, reverse=True)
    ranked = [sorted_avg.index(a) + 1 for a in sorted_avg]
    avg_rank_dict = {sorted_avg[i]: ranked[i] for i in range(len(sorted_avg))}
    answer = [avg_rank_dict[a] for a in avg_score]
    return answer