import random as r
from tkinter import *
#필요한 모듈 소환
window = Tk()
window.title('Guess Number Game')
lbl = Label(window, text="Guess Number Game")
lbl.pack()
result_input = 0
window.resizable(0,0)
random_number =  r.randint(0,100)
#맞출 숫자 선정 (랜덤함수)
pop_up = Label(window,text="숫자를 맞춰보세요!")
def panbul():
    result = int(result_input.get())
    if result == random_number:
        pop_up.configure(text ="성공!")
        success_game = True
    elif result > random_number:
        pop_up.configure(text ="너무 커요!")
    elif result < random_number:
        pop_up.configure(text ="너무 작아요!")
    else:
        pop_up.configure(text ="엥?")
    pop_up.pack()
    window.mainloop()
#판별을 위한 명령어

window.geometry("400x100")
success_game = False
command_button = Button(window, text='제출', command = panbul)
while success_game == False:
    result_input = Entry(window)
    result_input.pack()
    command_button.pack()
    window.mainloop()

#수업시간에 배웠던 random 함수와 스스로 탐구한 tkinter GUI 모듈을 이용하여
#기존에 만들었던 Guess Number Game을 더 강화하여 보았다.

