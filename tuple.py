# 튜플 : 변경할 수 없는 리스트 - literal list ?

# 튜플 생성
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) #(1, 2, 3, 4, 5)
type(tuple1) #<class 'tuple'>

tuple2 = 1, 2, 3
print(tuple2) #(1, 2, 3)
type(tuple2) #<class 'tuple'>

list1 = [1, 2, 3]
tuple3 = tuple(list1)
print(tuple3) #(1, 2, 3)

tuple3[0] #1
tuple3[1] #2

tuple3[0] = 5 #TypeError
del tuple3[3] #TypeError
tuple3.pop(0) #AttributeError


'''
Tuple

 - 튜플을 이용하는 이유
   + 변수간 값을 서로 변경할 때
   + 여러 값을 한번에 전달할 때 유용

 - 튜블 선언
    tuple1 = (1, 2, 3)
    tuple2 = 1, 2, 3
    tuple3 = tuple(list)

 - 튜플은 값의 변경과 삭제가 불가능
 
 - 한번 정해진 순서를 바꿀 수 없음

'''