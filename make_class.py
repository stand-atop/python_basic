
# 클래스 만들기

class Human():
    '''사람'''

person1 = Human()
person2 = Human() # 호출할 때마다 클래스가 사용됨

a = list()
print(a) #[]
print(isinstance(a,list)) #True

# 클래스 : 값을 저장하고 그 값을 변경함, 각각 클래스에 따라 정의된 특성이 다름
list1 = [1, 2, 3]
print(list1) #[1, 2, 3]
list1.append(4)
print(list1) #[1, 2, 3, 4]

person1.language = '한국어'
person2.language = 'English'

print(person1.language) #한국어
print(person2.language) #English

person1.name = '한국인'
person2.name = '영국인'

# 함수 사용
def speak(person):
    print("{}이 {}로 말함".format(person.name, person.language))

speak( person1 ) #한국인이 한국어로 말함
speak( person2 ) #영국인이 English로 말함

# 클래스에 함수를 넣을 수 있음
Human.speak = speak
person1.speak() #한국인이 한국어로 말함
person2.speak() #영국인이 English로 말함


'''
클래스
 - class 클래스명():
 - 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다
 - 클래스에 함수를 넣을 수 있다
'''


'''
클래스 만들기

클래스 선언
    class Human( ):
        ''구현''

인스턴스 생성
    person1 = Human( )
    person2 = Human( )
    
 - 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.
'''
