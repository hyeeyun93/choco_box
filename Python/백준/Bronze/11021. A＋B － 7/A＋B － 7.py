import sys

test_case = int(sys.stdin.readline().rstrip())

test_case_list = []

for _ in range(test_case):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    test_case_list.append((A+B))

for n in range(len(test_case_list)):
    print(f'Case #{n + 1}: {test_case_list[n]}')