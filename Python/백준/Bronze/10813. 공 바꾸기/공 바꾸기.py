import sys

N, M = map(int, sys.stdin.readline().split())
bags = [x for x in range(1, N+1)]

while M > 0:
    i, j = map(int, sys.stdin.readline().split())
    bags[i-1], bags[j-1] = bags[j-1], bags[i-1]
    M -= 1

print(*bags)