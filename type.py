
# 자료형 다루기


# 문자열
s = 'Hello Python'
print(type(s)) #<class 'str'>

# 소수
f = 3.14
print(type(f)) #<class 'float'>

# 정수
i = 31
print(type(i)) #<class 'int'>

print(type(31.0)) #<class 'float'>
31 == 31.0 #True

# 자료형 확인
isinstance(31, int) #True
isinstance(31, float) #False
isinstance(31.0, float) #True
isinstance(31.0, int) #True


'''
자료형 다루기

자료형
 - type( a ) # type( 변수명 ) : 자료형
 - isinstance( 42, int ) # isinstance( 값, 자료형 ) : 자료형 검사
'''
