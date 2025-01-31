word = input()
halved = len(word)//2
if len(word) % 2 == 0:
    if word[:halved] == word[-1:halved-1:-1]:
        print(1)
    else:
        print(0)
else:
    if word[:halved] == word[-1:halved:-1]:
        print(1)
    else:
        print(0)