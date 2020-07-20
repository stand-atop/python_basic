# break & continue

# break : 반복문의 중지
list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for val in list:
    if val % 3 == 0 :
        print(val)
        break
        
# continue : 제외하는 경우를 가장 먼저 처리해줌. 핵심 코드가 너무 하위로 내려가지 않도록 해줌
'''
for i in range(10):
    if i % 2 != 0 :
        print(i)
        print(i)
        print(i)
        print(i)
'''
for i in range(10) :
    if i % 2 == 0 :
        continue
    print(i)
    print(i)
    print(i)
    print(i)
    
    
'''
break, continue
 - break : 반복문을 종료시킴
 - continue : 반복문의 나머지 부분을 보이지 않고 반복문의 처음으로 돌아감
 - for문과 while문에서 똑같이 작동함
'''    



'''
break, continue

break
 - 반복문을 종료시키는 기능

continue
 - 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능
'''