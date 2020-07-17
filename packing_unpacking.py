
# packing, unpacking

# tuple을 이용해 하나의 변수에 여러개의 변수를 저장할 수 있다
# packing : 하나의 변수에 여러개의 값을 넣음
# unpacking : packing 된 변수에서 여러개의 값을 꺼내옴
# 변수 교환에 용이함
# 함수에서 여러개의 값을 한번에 return 받을 때 유용함

a, b = 1, 2 #a와 b로 이루어진 tuple이 생성되고, 1과 2로 이루어진 tuple이 생성됨. (=)대입연산자를 통해 a에는 1, b에는 2가 대입됨. tuple끼리 대입한 것
print(a, b) #1 2

# unpacking
c = (3, 4)
print(c) #(3, 4)
d, e = c
print(d) #3
print(e) #4

# packing
f = d, e
print(f) #(3, 4)



# 일반적 변수 교환
x = 5
y = 10
temp = x
x = y
y = temp
print(x, y) #10 5

# packing, unpacking을 이용한 교환
x, y = y, x
print(x, y) #5 10


# 함수에서 여러개의 값을 한번에 return
def tuple_func():
    return 1, 2
q, w = tuple_func()
print(q, w) #1 2



'''
packing, unpacking
 - 하나의 변수에 여러개의 변수 대입 가능
 - 함수의 리턴 값으로 여러 값을 전달 할 수 있다
'''



'''
packing, unpacking

packing
 - 하나의 변수에 여러개의 값을 넣는 것

unpacking
 - 패킹된 변수에서 여러개의 값을 꺼내오는 것
        c = (3, 4)
        d, e = c    # c의 값을 언패킹하여 d, e에 값을 넣었다
        f = d, e    # 변수 d와 e를 f에 패킹

튜플의 활용
 - 두 변수의 값을 바꿀 때 임시변수가 필요 없다.
 - 함수의 리턴 값으로 여러 값을 전달할 수 있다.
'''