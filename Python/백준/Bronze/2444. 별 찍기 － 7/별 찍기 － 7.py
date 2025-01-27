N = int(input())
for i in range(N):
    print(' ' * (N-1-i) + '*' * (i+1) + '*' * i)
for j in range(N-2, -1, -1):
    print(' ' * (N-1-j) + '*' * (j+1) + '*' * j)