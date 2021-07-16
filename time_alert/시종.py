#개인프로젝트
# '원격수업 시종프로그램'
#1. 각 교시별로 어떠한 과목이 있는지 입력받음 (과목이 존재하지 않을 경우 해당 교시에는 시종하지 않는것으로 판단
#2. 매 15초마다 현재 분이 00분 또는 10분인지 (오후/오전), 현재 시각 (ex: 09시 등)이 정규 수업시간 안에 존재하는지 판단
#3. 00분 또는 10분 도달시 학교종 음악이 시행된 후 현재 과목 Pop-up 표시
#4. '음악 재생중' 에는 프로그램이 응답 없음 상태가 됨. Threading 관련 문제로 추정하나 현재 수준에선 고칠 방법 없음

#탐구 동기: 원격수업 특성상 어떠한 알림도 주지 않기에 소리등을 통해서 수업 시작 시간을 알 수 있으면
#원격수업 결시율이나 지각율이 떨어지지 않을까 생각하여 제작하게 되었다.

#제작 기간 07-14 ~ 07-14
#느낀점: 보기엔 간단한 프로그램도 엄청나게 복잡한 구조를 가지고 있음을 깨달았고, pickle 등 모듈을 통한
#외부 파일로의 저장, 불러오기를 배우게 됐으며, GUI 개발에 더욱 친숙해 진 것 같다.
import time
import os.path
import pickle
import sys
#encoding=utf-8
import io
from playsound import playsound
#타종 재생을 위한 모듈입니다. 별도로 설치해 주세요.
from tkinter import *
from tkinter import messagebox

sys.setrecursionlimit(1000000000)

root = Tk()
root.title("원격수업 시종알리미")
root.geometry("400x300")
root.resizable(True,True)

def Clear():
    mylist = root.grid_slaves()
    for i in mylist:
        i.destroy()
#창에 있는 모든 Entry, Label 제거
def DayGet():
    global today
    tempday = time.strftime('%a',time.localtime(time.time()))
    if tempday == 'Mon':
        today = '월요일'
    elif tempday == 'Tue':
        today = '화요일'
    elif tempday == 'Wed':
        today = '수요일'
    elif tempday == 'Thu':
        today = '목요일'
    elif tempday == 'Fri':
        today = '금요일'
    elif tempday == 'Sat':
        today = '토요일'
    elif tempday == 'Sun':
        today = '일요일'
#영문으로 받아온 요일 (tempday)를 한글로 변경하는 함수
def SubjSetting():
    NowSelected = listboxD.get(ACTIVE)
    Clear()
    for i in range(1,8,1):
        globals()["sub{}".format(i)] = ""
    Label(root, text="교시 별 과목명을 입력해 주세요, 비어있는 교시는 시종하지 않습니다.").grid(row = 0, column = 1, padx = 5, pady = 5)
    for i in range(0,7,1):
        Label(root, text=str((i+1)) + "교시 : ").grid(row = (i+1), column = 0, padx = 5, pady = 5)
        globals()["sub{}".format(i+1)] = Entry(root)
        globals()["sub{}".format(i+1)].grid(row = (i+1), column = 1, padx = 5, pady = 5)
    def SaveSubjSett():
        txtname = NowSelected + "Subj" + ".txt"
        subj_list = []
        with open (txtname,'wb') as file:
            for i in range(1,8,1):
                sample_list = [i,globals()["sub{}".format(i)].get()]
                subj_list.append(sample_list)
            pickle.dump(subj_list,file)
        SettingOK()
    SubjButton = Button(root, text="저장",command=SaveSubjSett).grid(row=9, column = 1)
#각 교시별 입력하는 함수.
#입력받은 후 pickle 을 이용하여 [['1','(과목명)'],['2','(과목명)']] 과 같이 저장
#입력하지 않을경우 '' 로 처리
#아래의 SubjDays 함수에서 선택한 요일 (NowSelected) + Subj.txt의 형태로 저장 (ASCII 형식으로 저장되기에 평범하게 읽을 수 없음)
def SubjDays():
    Clear()
    global listboxD
    Label(root, text="설정할 요일을 입력하세요").grid(row=0)
    Label(root, text="오늘은 " + today + " 입니다").grid(row=1)
    listboxD = Listbox(root, selectmode='single')
    listboxD.grid(row=2)
    listboxD.insert(0, '월요일')
    listboxD.insert(1, '화요일')
    listboxD.insert(2, '수요일')
    listboxD.insert(3, '목요일')
    listboxD.insert(4, '금요일')
    DayButton = Button(root, text="선택",command=SubjSetting).grid(row=3)
#저장할 시간표의 요일을 정하는 리스트
#월~금까지 존재하며, 선택 버튼을 누르면 위의 SubjSetting 실행
def GetNowHour():
    global Nowhour, Nowminute
    Nowhour = time.strftime('%H', time.localtime(time.time()))
    Nowminute = time.strftime('%M', time.localtime(time.time()))
#현재 시간을 구해서 전역변수로 선언하는 함수
def TimeAlarm(x):
    global now_gosi
    playsound("alarm.mp3")
    NowTry = x + 1
    txtname = today + "Subj" + ".txt"
    with open (txtname,'rb') as file:
        list_today = pickle.load(file, encoding = 'utf-8')
    now_gosi = list_today[x][1]
#시간이 되어 호출되면 alarm.mp3를 재생하고 기존에 제작했던 과목 리스트를 불러들여 현재 시간의 과목을 전역변수로 지정함
def StartAlarm():
    Clear()
    txtname = today + "Subj" + ".txt"
    checkFileExist = os.path.exists(txtname)
    if checkFileExist == False:
        messagebox.showinfo("시간별 과목정보 파일 미존재",today + " 파일이 존재하는지 다시한번 확인하세요.")
        root.after(10,SettingOK)
    global Hourstart, DestTime
    DestTime = ''
    Hourstart = ['09','10','11','12','14','15','16']
    Passhour = []
    if today == '토요일' or today == '일요일':
        messagebox.showinfo("주말 과목정보 미존재",today + " 주말은 정규수업이 존재하지 않습니다.")
        root.after(10,SettingOK)
    Label(root, text="시종 작동중").grid(row = 0, column = 1, padx = 5, pady = 5)
    with open (txtname,'rb') as file:
        list_today_n = pickle.load(file, encoding = 'utf-8')
    for i in range (0,7,1):
        if list_today_n[i][1] == '':
            Passhour.append(Hourstart[i])
            #print(i)
    def AlarmLoop():
        global HourIndex, DestTime
        GetNowHour()
        if Nowhour in Hourstart and Nowhour not in Passhour:
            HourIndex = Hourstart.index(Nowhour)
            if HourIndex <= 3:
                DestTime = '10'
            else:
                DestTime = '00'
        if Nowminute == DestTime and Nowhour not in Passhour:
            TimeAlarm(HourIndex)
            #print('Alarm')
            Label(root, text="현재 과목 :" + str(now_gosi) + " , 현재 교시 :" + str(HourIndex + 1)).grid(row = 2, column = 1, padx = 5, pady = 5)
            messagebox.showinfo(str(HourIndex + 1) + "교시 알림",str(now_gosi) +" 수업을 이수하세요!")
            Passhour.append(Hourstart[HourIndex])
        Label(root, text="현재 시각 :" + Nowhour + "시" + Nowminute + "분").grid(row = 1, column = 1, padx = 5, pady = 5)
        Loop2()
        root.mainloop()
    def Loop2():
        root.after(15000, AlarmLoop)
    AlarmLoop()
#1. 시간별 과목정보 파일이 존재하지 않거나 주말일 경우에는 Pop-up창 띄우고 초기상태로 원복
#2. 과목 리스트를 불러들인 다음 [1] 번 index에 존재하지 않는경우 (''인 경우. 즉, 입력하지 않은경우)에는 Passhour 리스트에 추가해
#시종되지 않도록 지정함.
#본래는 time.sleep 구문 및 While 문을 사용할려고 노력하였으나 GUI 상에서는 Threading 상의 이유로 작동하지 않음. (또는 작동해도 프로그램 미응답)
#여러 노력 끝에 .after 구문을 사용해서 15초 간격으로 상호간에 호출하도록 구현하였음.
# 그외, 현재 시간의 Index 값이 3 이하면 (오전이면) DestTime 을 10으로 지정하여 10분에 타종하도록 설정, 오후라면 00분에 타종하도록 설정
#현재 시간이랑 DestTime 이 동일하면 TimeAlarm 함수를 실행하여 소리 재생, 과목과 현재 교시를 Pop-up 창으로 띄우고
#15초 후이면 다시 재생될 수 있으므로 Passhour 리스트에 현재 시간을 append 함으로써 다시 재생되는것을 방지함.
def SettingOK():
    Clear()
    Bbutton = Button(root, text="수업 시간 별 과목 설정",command=SubjDays).grid(row=1, column = 1)
    Cbutton = Button(root, text="시종 작동 시작!",command = StartAlarm).grid(row=2, column = 1)
#최초 화면
DayGet()
SettingOK()
root.mainloop()
