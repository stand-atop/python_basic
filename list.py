
# 리스트 : 배열
list1 = ['가위', '바위', '보']
list2 = [1,2,3,4,5,6,7,8]

print(list1) #['가위', '바위', '보']
print(list2) #[1, 2, 3, 4, 5, 6, 7, 8]

print(list1[0]) #가위
print(list1[1]) #바위
print(list1[2]) #보

print(list2[0]) #1



# list 값의 변경
list1[0] = '바위'
print(list1[0]) #바위
print(list1) #['바위', '바위', '보']

# list 호출 : 개수 내에서 앞/뒤에서 호출할 수 있음
print(list1[3]) #error
print(list1[-1]) #보
print(list1[-2]) #바위
print(list1[-3]) #바위
print(list1[-4]) #error



'''
리스트 사용

List
 - 여러개의 값을 담을 수 있는 변수
   + list1 = [1,2,3,4,5]

 - 값 읽어오기
   + 리스트를 사용할때는 0번째가 첫번째
   + 첫번째 값 list1[0]
   + 두번째 값 list1[1]
   + 뒤에서 첫번째 값 list1[-1]
   + 뒤에서 두번째 값 list1[-2]
   + 리스트에 들어있는 값 보다 큰 값을 읽어오려고 하면 에러
        예. 위의 list1에서 list1[5] 또는 list1[-6]은 에러

 - 값 쓰기
   + 변수와 같이 list1[0]=10이라고 하면 list의 첫번째 값이 10으로 변경
'''