import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt 
check = False
while check == False:
    선택지 = int(input('선택지(1: 기본, 2: 평균별, 3: 표준편차별, 4: 문제02, 6: 종료): '))
    if 선택지 == 6:
        check = True
        break   
    평균 = int(input('평균은 몇? : '))
    표준편차 = int(input('표준편차는 몇? ; '))
    if 선택지 == 2 or 선택지 == 3:
        if 선택지 == 2:
            print('변수1 : 1, 변수2 : 2 추천')
        else:
            print('변수1 : 2, 변수2 : 3 추천')
        변수1 = int(input('변수1 ? :'))
        변수2 = int(input('변수2 ? :'))
    if 선택지 == 4:
        plt.axhline(y=0.40, color='r', linestyle='--', linewidth=1)
        plt.axvline(x=2, color='y', linestyle='--', linewidth=1)
    x = np.linspace(-3, 3, 200)
    y = stats.norm(평균,표준편차).pdf(x)
    if 선택지 == 2:
        y1 = stats.norm(변수1,1).pdf(x)
        y2 = stats.norm(변수2,1).pdf(x)
    elif 선택지 == 3:
        y1 = stats.norm(0,변수1).pdf(x)
        y2 = stats.norm(0,변수2).pdf(x)
    elif 선택지 == 4:
        y1 = stats.norm(2,1).pdf(x)
        y2 = stats.norm(2,1.5).pdf(x)
        print('주황색 평균 = 2, 표준편차 = 1')
        print('연두색 평균 = 2, 표준편차 = 2')
    elif 선택지 == 5:
        크기 = int(input('표본평균의 크기는? :'))
        크기루트 = 크기**(1/2)
        y1 = stats.norm(평균,표준편차/크기루트).pdf(x)
    plt.plot(x,y)
    if 선택지 == 2 or 선택지 == 3 or 선택지 == 4:
        plt.plot(x,y1)
        plt.plot(x,y2)
    elif 선택지 == 5:
        plt.plot(x,y1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
