word = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
answer = []

for c in alphabet:
    if c in word:
        answer.append(word.index(c))
    elif c not in word:
        answer.append(-1)

print(*answer)