import sys

user_input = int(sys.stdin.readline().rstrip())

for n in range(1, user_input + 1):
    print(n * '*')
    n += 1