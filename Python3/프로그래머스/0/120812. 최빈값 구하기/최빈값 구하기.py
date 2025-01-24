def solution(array):
    counts = {}
    for n in array:
        counts[n] = counts.get(n, 0) + 1

    if len(counts) == 1:
        return array[0]
    elif sum(1 for value in counts.values() if value == max(counts.values())) > 1:
        return -1
    else:
        return max(counts, key=counts.get)