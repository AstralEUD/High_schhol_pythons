#십진수 - 이진수 변환기
n = int(input('변환할 십진수는?: '))
first = n
divide = False
result = []
whileOut = False
checkCount = 0
ResultValue = str()
while whileOut == False:
    if n//2 != 0:
        divide = True
    else:
        result.append("1")
        checkCount += 1
        whileOut == True
        break
    if n%2 == 0 and divide == True:
        result.append("0")
        n = n//2
        checkCount += 1
    elif n%2 == 1 and divide == True:
        result.append("1")
        checkCount += 1
        n = n//2
    #print(result)
for i in range(0,checkCount,1):
    ResultValue = str(ResultValue) + str(result.pop())
print(first,'(10) 의 이진수 변환 형태는',ResultValue,'(2)')
        
#이진수 - 십진수 변환기
n = str(input('변환할 이진수는?: '))
second = n
nlist2 = list(n)
countlist = len(nlist2)
print(countlist, nlist2)
result = 0
for a in range(0,countlist,1):
    result = result + ((2**a) * int(nlist2.pop()))
print(result)
