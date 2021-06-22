list_bubble = [['aaa',180,86],['bbb',163,85],['ccc',182,67],['ddd',159,73],['eee',173,95]]
list_copy = list_bubble[:]

a = 0
e = 2
c = 1
bubble_check = False
check_b = False
#최소 순 정렬
#버블 정렬 (bubble sort)
while check_b == False:
    a = 0
    count_list = len(list_bubble) - c
    while bubble_check == False:
        if list_copy[a][e] > list_copy[a+1][e]:
            temp1 = list_copy[a]
            temp2 = list_copy[a+1]
            list_copy[a] = temp2
            list_copy[a+1] = temp1
            print('changing')
            if a > 2:
                a = a-2
        elif list_copy[a][e] < list_copy[a+1][e]:
            print('OK')
        a += 1
        if a == len(list_bubble) - 1:
            bubble_check = True
    bubble_check = False
    c += 1
    if c == 5:
        check_b = True
    print('Now List: ',list_copy)
print('=============\n버블 정렬 결과\n==============')
print(list_copy,"\n"*5)

list_copy2 = list_bubble[:]
#선택정렬 (selection sort)
g = 0
check_a = False
while check_a == False:
    maxcomp = maxva = 0
    for a in range(g,len(list_bubble),1):
        if a == g:
            maxcomp = list_copy2[a][e]
        elif list_copy2[a][e] < maxcomp:
            maxva = list_copy2[a]
            maxcomp = list_copy2[a][e]
    print('Now Min: ',maxva)
    print('Turn: ',g)
    list_copy2.remove(maxva)
    list_copy2.insert(g,maxva)
    print('Now List: ',list_copy2)
    g += 1
    if g == len(list_bubble) - 2:
        check_a = True
print('==============\n선택 정렬 결과\n===============')
print(list_copy2,"\n"*5)
        
#삽입 정렬 (insert sort)
list_copy3 = list_bubble[:]
check_d = False
now_index = len(list_copy3) - 1
while check_d == False:
    temp_list = list_copy3[:]
    for a in range(0,len(list_copy3),1):
        if list_copy3[now_index][e] > list_copy3[a][e]:
            print(list_copy3[now_index][e],'are > ',list_copy3[a][e])
        elif list_copy3[now_index][e] < list_copy3[a][e]:
            temp_insertion = list_copy3[now_index]
            list_copy3.remove(temp_insertion)
            list_copy3.insert(a-1,temp_insertion)
    now_index -= 1
    print(list_copy3)
    if now_index == 0:
        check_d = True
print('='*10,'\n삽입 정렬 결과\n','='*10)
print(list_copy3)



#ref : https://www.daleseo.com/sort-insertion/

