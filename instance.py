 
 # 인스턴스

# 정수 
print(type(5)) #<class 'int'>
print(isinstance(5, float)) #False

numbers1 = []
print(type(numbers1)) #<class 'list'>
numbers2 = list(range(10))
print(numbers2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 문자열
characters = list("hello")
print(characters) #['h', 'e', 'l', 'l', 'o']

# 인스턴스 확인
print(type(numbers2)) #<class 'list'>
print(type(characters)) #<class 'list'>

print(isinstance()numbers1, list) #True
print(numbers1 == list) #False

'''
인간 클래스
 - 철수 인스턴스
 - 영희 인스턴스

List 클래스
 - numbers1 인스턴스
 - numbers2 인스턴스
'''


'''
인스턴스 이해

클래스
 - 함수나 변수들을 모아 놓은 집합체

인스턴스
 - 클래스에 의해 생성된 객체
 - 인스턴스 각자 자신의 값을 가지고 있다.
'''


'''
값을 비교
 - a == b

인스턴스 비교
 - a is b
'''