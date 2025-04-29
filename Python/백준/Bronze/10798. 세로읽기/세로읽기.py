word_list = []

for i in range(5):
    n = input()
    word_list.append(n)

answer = ""

for l in range(15):
    for n in range(5):
        try: 
            answer += word_list[n][l]
        except IndexError: pass
                
print(answer)