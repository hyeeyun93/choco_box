N = int(input())
numlist = map(int, input().split())
v = int(input())
count = 0
for num in numlist:
    if v == num:
        count += 1
print(count)