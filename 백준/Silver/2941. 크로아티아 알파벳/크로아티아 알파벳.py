words_input = input()
croatia_alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

words_input = words_input.replace('dz=', '*')

for c in croatia_alpha:
    words_input = words_input.replace(c, '*')

print(len(words_input))