n = int(input())

squares = []

for _ in range(n):
    x, y = map(int, input().split())
    squares.append((x, y))

non_overlap = set()

for x, y in squares:
    for i in range(x, x+10):
        for j in range(y, y+10):
            non_overlap.add((i, j))

print(len(non_overlap))