import sys

calc_list = []
count = 0

while count < 10:
    num_input = int(sys.stdin.readline())
    remainder = num_input % 42
    if remainder not in calc_list:
        calc_list.append(remainder)
    count += 1

print(len(calc_list))