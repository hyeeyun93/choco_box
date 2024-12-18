a, b, c = map(int, input().split())
if a == b == c:
    reward1 = 10000 + a * 1000
    print(reward1)
elif a == b or a == c or b == c:
    if a == b or a == c:
        reward2 = 1000 + a * 100
        print(reward2)
    elif b == c:
        reward3 = 1000 + b * 100
        print(reward3)
elif a != b != c:
    reward4 = max([a, b, c]) * 100
    print(reward4)