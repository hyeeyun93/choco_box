def solution(arr, idx):
    answer = 0
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i
            break
        elif 1 not in arr[idx:]:
            answer = -1
    return answer