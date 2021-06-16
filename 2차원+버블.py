list_name = [["홍길동",175,80],["김철수",182,75],["박기순",152,90],["최기원",192,66],["시윤석",165,57],["외모지",147,98],["김바진",190,85]]
list_new = list_name[:]
#버블 정렬
#작은것부터 정렬
e = 2
print('몸무게 순 정렬 (버블)')
print(list_new)
a = 0
bubble_check = False
while bubble_check == False:
    print(a,'\n')
    if list_new[a][e] > list_new[a+1][e]:
        print(list_new[a][0],'are bigger than',list_new[a+1][0])
        print(list_new[a][0],'are changing position with',list_new[a+1][0])
        print(list_new,'\n')
        temp1 = list_new[a]
        temp2 = list_new[a+1]
        list_new[a] = temp2
        list_new[a+1] = temp1
        print(temp1, temp2,a)
        if list_new[a][e] < list_new[a-1][e]:
            a = a-1
    elif list_new[a][e] < list_new[a+1][e]:
        print(list_new[a][0],'are smaller than',list_new[a+1][0])
    else:
        print(list_new[a][0],'are same with',list_new[a+1][0])
        a = a+1
    if a+1 == len(list_name)-1:
        break
    a += 1
    print(a,'\n')   
print(list_new)

        
    
