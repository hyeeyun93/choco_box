import sys

N, M = map(int, sys.stdin.readline().split())
bags = [0 for _ in range(N)]

while M > 0:
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i-1, j):
        bags[x] = k
    M -= 1

print(' '.join(map(str, bags)))