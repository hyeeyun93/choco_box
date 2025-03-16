one_line = []

for _ in range(9):
    rows = map(int, input().split())
    for n in rows:
        one_line.append(n)

biggest = max(one_line)
index = one_line.index(biggest)
row = (index // 9) + 1
column = (index % 9) + 1

print(biggest)
print(f'{row} {column}')