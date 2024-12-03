import random
import time

while True:
    print('='*50)
    print('%25s' % ('숫자 맞추기 게임'))
    print('='*50)
    print('1.시작\n2.종료')
    try:
        ask = int(input('메뉴를 선택해주세요: '))
    except ValueError:
        print('오류! 숫자만 입력하세요!')
        time.sleep(1)
        continue
    if ask == 1:
        time.sleep(1)
        print('1부터 10 사이의 숫자를 입력하세요')        
        i = random.randint(1,10)
        while True:
            try:
                guess = int(input('입력: '))
            except ValueError:
                print('오류! 숫자만 입력하세요!')
                time.sleep(1)
                continue
            if guess < 1 or guess > 10:
                print('오류! 1부터 10 사이의 숫자만 입력하세요!')
                time.sleep(1)
            elif i < guess:
                print('숫자가 너무 커요.')
                time.sleep(1)
            elif i > guess:
                print('숫자가 너무 작아요.')
                time.sleep(1)
            else:
                print('정답입니다!')
                time.sleep(1)
                break
    elif ask == 2:
        print('게임을 종료합니다')
        quit()
    else:
        print('없는 메뉴입니다. 다시 선택하세요')
        time.sleep(1)