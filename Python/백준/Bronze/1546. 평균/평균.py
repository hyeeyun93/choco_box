N = int(input())
score_list = list(map(int, input().split()))
M = max(score_list)
new_score = []

for i in score_list:
    new_score.append(i / M * 100)

print(sum(new_score)/N)