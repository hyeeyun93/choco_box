dial = {2:['A','B','C'],
        3:['D','E','F'],
        4:['G','H','I'],
        5:['J','K','L'],
        6:['M','N','O'],
        7:['P','Q','R','S'],
        8:['T','U','V'],
        9:['W','X','Y','Z']}

phoneword = list(input())
phonenumber = []
for c in phoneword:
    for k, v in dial.items():
        if c in v:
            phonenumber.append(k)
dialtime = 0
for n in phonenumber:
    dialtime += n + 1
print(dialtime)