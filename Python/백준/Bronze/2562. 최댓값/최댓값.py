import sys

count = 0
numlist = []

while count != 9:
    N = int(sys.stdin.readline())
    numlist.append(N)
    count += 1

max_num = max(numlist)
print(max_num)
print(numlist.index(max_num) + 1)