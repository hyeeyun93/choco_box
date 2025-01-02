import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
checklist = []

for i in range(N):
    if A[i] < X:
        checklist.append(A[i])
print(*checklist)