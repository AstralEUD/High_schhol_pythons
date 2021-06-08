import random as r
Game_over = False
Game_count = 0
while Game_over == False:
    ghost = r.randint(1,3)
    open_room = int(input('몇번 문을 여시겠습니까 (1/2/3): '))
    if open_room == ghost:
        print('Wow! You meet him!')
        print('Game count :',Game_count)
        break
    else:
        print('You failed it!')
        Game_count += 1
        
