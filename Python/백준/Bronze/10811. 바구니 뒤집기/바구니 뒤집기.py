N, M = map(int, input().split())
bag = [x for x in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    bag[i-1:j] = bag[i-1:j][::-1]

print(*bag)