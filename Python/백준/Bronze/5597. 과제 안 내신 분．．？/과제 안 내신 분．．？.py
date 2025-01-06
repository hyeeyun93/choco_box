import sys

checklist = []

for _ in range(28):
    n = int(sys.stdin.readline())
    checklist.append(n)

for i in range(1, 31):
    if i not in checklist:
        print(i)