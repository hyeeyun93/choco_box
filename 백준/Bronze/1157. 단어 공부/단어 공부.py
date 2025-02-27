text = input().upper()
char_counts = {}

for ch in text:
    char_counts[ch] = char_counts.get(ch, 0) + 1

char_max_count = []
for key, value in char_counts.items():
    if value == max(char_counts.values()):
        char_max_count.append(key)

if len(char_max_count) > 1:
    print('?')
else:
    print(char_max_count[0])