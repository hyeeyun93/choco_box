X = int(input())
N = int(input())

item_price = []
for _ in range(N):
    a, b = map(int, input().split())
    item_price.append(a * b)

if sum(item_price) == X:
    print('Yes')
else:
    print('No')