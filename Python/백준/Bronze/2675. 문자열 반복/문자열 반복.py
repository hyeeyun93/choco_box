T = int(input())

for _ in range(T):
    R, S = input().split()
    print(''.join(c * int(R) for c in S))