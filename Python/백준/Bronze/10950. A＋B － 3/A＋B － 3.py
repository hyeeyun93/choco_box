test_case = int(input())
test_case_list = []
for _ in range(test_case):
    A, B = map(int, input().split())
    test_case_list.append((A, B))
    
for i in range(len(test_case_list)):
    print(test_case_list[i][0] + test_case_list[i][1])