def solution(my_string):
    my_string_list = list(my_string)
    num_list = []
    nums = ''

    for i in range(len(my_string_list)):
        if my_string_list[i].isdigit():
            nums += my_string_list[i]
        else:
            if nums:
                num_list.append(int(nums))
                nums = ''

    if nums:
        num_list.append(int(nums))
    answer = sum(num_list)

    return answer