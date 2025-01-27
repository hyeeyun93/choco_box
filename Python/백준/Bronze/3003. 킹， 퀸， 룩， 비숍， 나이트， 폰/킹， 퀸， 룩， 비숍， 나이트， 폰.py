check = [1, 1, 2, 2, 2, 8]
piece = [int(p) for p in input().split()]
print(' '.join(str(c - p) for c, p in zip(check, piece)))