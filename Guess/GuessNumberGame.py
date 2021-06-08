#Guess Number Game 기본
import random as r
import time
print('=== Guess Number Game ===\n')
randomfx = r.randint(1,100)
count = 0
victory = False
starttime = time.time()
while victory != True:
    print('1부터 100까지의 숫자를 입력하세요')
    answer = int(input('입력: '))
    if answer == randomfx:
        print('성공!')
        victory = True
    elif answer > randomfx:
        print('높음!')
        count += 1
    elif answer < randomfx:
        print('낮음!')
        count += 1
    else:
        print('오류!')
print(count,'번의 시도 끝에 성공')
print(round(time.time() - starttime),'초 만에 성공')
