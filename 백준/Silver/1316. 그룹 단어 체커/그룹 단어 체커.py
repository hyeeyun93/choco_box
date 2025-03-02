N = int(input())
answer = N

for _ in range(N):
    words = input()
    seen = set()
    prev_char = ''

    for c in words:
        if c in seen and c != prev_char:
            answer -= 1
            break
        seen.add(c)
        prev_char = c

print(answer)
