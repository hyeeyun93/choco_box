import string

def solution(age):
    answer = ''
    age_numbers = []
    alien_age = list(string.ascii_lowercase)
    for d in str(age):
        age_numbers.append(int(d))
    for n in age_numbers:
        answer = answer + alien_age[n]
    return answer