import sys

N = int(sys.stdin.readline())
checklist = list(map(int, sys.stdin.readline().split()))

print(min(checklist), max(checklist))