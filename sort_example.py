import time
import string
import random
list_bubble = [['aaa',180,86],['bbb',163,85],['ccc',182,67],['ddd',159,73],['eee',173,95]] #5개의 리스트 비교
#list_bubble = [['aaa',180,86],['bbb',163,85],['ccc',182,67],['ddd',159,73],['eee',173,95],['fff',196,77],['ggg',154,56],['hhh',193,96],['iii',163,50]] #9개의 리스트 비교

#다음 for문은 대형 record 테스트를 위한 구문입니다.
for a in range(50):
    stringt = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    list_bubble.append([stringt,random.randint(150,190),random.randint(50,100)])
print(list_bubble)
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
print('소모 시간: ',round(bubble_time,5),'\n'*2)

#버블 정렬은 첫번째 자료와 두번째 자료를 비교하고, 두번째 자료와 세번째 자료를 비교하고, (리스트의 개수 - 1) 번째 자료와 (리스트의 개수) 자료를 비교하게 된다. (회전)
#한 후 1회전이 끝나서 가장 큰 수가 마지막 칸에 있으면 다시 처음부터 첫번째 자료와 두번째 자료를 비교하되,
#(리스트의 갯수) - (회전수)까지 비교하여 회전수가 (리스트의 개수 - 1)이 되면 중단한다.
#버블 정렬은 구현이 매우 간단하나, 교환 작업의 복잡도로 인해 잘 사용되지 않는다.

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
    if maxva == 0:
        check_a = True
        break
    print('Turn: ',g)
    list_copy2.remove(maxva)
    list_copy2.insert(g,maxva)
    print('Now List: ',list_copy2)
    g += 1
    if g == len(list_copy2) - 2:
        check_a = True
print('==============\n선택 정렬 결과\n===============')
print(list_copy2)
selection_end_time = time.time()
selection_time = selection_end_time - selection_start_time
print('소모 시간: ',selection_time,'\n'*2)

#선택 정렬은 모든 리스트 값에서 최소값을 탐색하여, 해당 값을 추출, 맨 앞에 넣고,
#(회전수 + 1) 번째 값부터 다시 모든 리스트에서 값을 검색하게 된다.
#최종적으로 회전수 값이 (리스트 개수 - 1) 이 되면 비교를 중단한다.
#구현이 간단하고, 역순 정렬에서 매우 유리한 결과를 보여주나, 이미 정렬된 상태에서
#소수의 자료만을 추가할 때에도 모든 리스트에서 탐색해야 하므로, 비효율적일 수 있다.

        
#삽입 정렬 (insert sort)
list_copy3 = list_bubble[:]
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

#처음 두개의 자료를 비교하여, 낮은 값을 앞으로 두고 (비교)
#탐색의 범위를 한개씩 늘려가서, 탐색의 범위가 리스트의 갯수와 동일하면 탐색을 중단한다.
#안정적인 정렬방법이며, 리스트의 개수가 적으면 더욱 효율적인 방법이다. 

print('버블 정렬 소모 시간 : ',round(bubble_time,3))
print('선택 정렬 소모 시간 : ',round(selection_time,3))
print('삽입 정렬 소모 시간 : ',round(insert_time,3))

#9개의 리스트를 바탕으로 실험:
#버블 정렬 : 0.545
#선택 정렬 : 0.394
#삽입 정렬 : 0.29

#5개의 리스트를 바탕으로 실험:
#버블 정렬 : 0.241
#선택 정렬 : 0.149
#삽입 정렬 : 0.114

#55개의 리스트를 바탕으로 실험:
#버블 정렬 : 7.69
#선택 정렬 : 5.459
#삽입 정렬 : 6.623

