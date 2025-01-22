def solution(a, b):
    cd = []
    for i in range(1, int(max(a, b)/2)+1):
        if a % i == 0 and b % i == 0:
            cd.append(i)
    gcd = max(cd)
    simplest_b = int(b/gcd)
    while simplest_b % 2 == 0:
        simplest_b //= 2
    while simplest_b % 5 == 0:
        simplest_b //= 5
    if simplest_b == 1:
        return 1
    else:
        return 2