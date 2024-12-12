x = int(input())
y = int(input())
y_list = [int(c) for c in str(y)]

for d in y_list[::-1]:
    ans = d * x
    print(ans)
print(x * y)