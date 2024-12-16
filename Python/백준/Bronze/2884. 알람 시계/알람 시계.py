(H, M) = map(int, input().split())
new_M = M - 45
if new_M < 0:
    if H-1 < 0:
        print(H + 23, new_M + 60)
    else:
        print(H-1, new_M + 60)
else:
    print(H, new_M)