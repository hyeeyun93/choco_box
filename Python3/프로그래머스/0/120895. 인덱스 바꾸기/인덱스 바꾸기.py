def solution(my_string, num1, num2):
    answer = ''
    char_list = list(my_string)
    char_list[num1], char_list[num2] = char_list[num2], char_list[num1]
    return answer.join(char_list)
