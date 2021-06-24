import time
list_bubble = [['aaa',180,86],['bbb',163,85],['ccc',182,67],['ddd',159,73],['eee',173,95]]
list_copy = list_bubble[:]

a = 0
e = 2
c = 1
bubble_check = False
check_b = False
#최소 순 정렬
#버블 정렬 (bubble sort)
bubble_start_time = time.time()
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
print(list_copy)
bubble_end_time = time.time()
bubble_time = bubble_end_time - bubble_start_time
print('소모 시간: ',bubble_time,'\n'*2)

list_copy2 = list_bubble[:]
#선택정렬 (selection sort)
g = 0
check_a = False
selection_start_time = time.time()
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
print(list_copy2)
selection_end_time = time.time()
selection_time = selection_end_time - selection_start_time
print('소모 시간: ',selection_time,'\n'*2)

        
#삽입 정렬 (insert sort)
list_copy3 = list_bubble[:]
check_d = False
insert_start_time = time.time()
print('초기 리스트: ',list_copy3)
for i in range(1,len(list_copy3),1):
    for q in range (1,i+1,1):
        if list_copy3[q-1][e] > list_copy3[q][e]:
            print(list_copy3[q-1],'가 ',list_copy3[q],'보다 큼')
            store1 = list_copy3[q-1]
            list_copy3[q-1] = list_copy3[q]
            list_copy3[q] = store1
print('='*10,'\n삽입 정렬 결과\n','='*10)
insert_end_time = time.time()
insert_time = insert_end_time - insert_start_time
print(list_copy3)
print('소모 시간: ',insert_time,'\n'*2)

#ref : https://www.daleseo.com/sort-insertion/

