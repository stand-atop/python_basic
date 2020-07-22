
# 메소드

# 클래스 만들기
class Human():
    '''사람'''

    # 사람 만들기
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    # 먹기
    def eat(self):
        self.weight += 0.5
        print("{}이 먹어서 {}kg가 됨".format(self.name, self.weight))

    # 걷기
    def walk(self):
        self.weight -= 0.5
        print("-내부- {}이 걸어서 {}kg가 됨".format(self.name, self.weight))
        
    # 말하기 : self외의 매개변수가 있을 때
    def speak(self, message):
        print(message)


person = Human.create('Tom', 65)
#person.walk() #Tom가 걸어서 64.5kg가 됨
#person.eat() #Tom가 걸어서 65.0kg가 됨
#person.walk() #Tom가 걸어서 64.5kg가 됨

# 클래스 외부 함수일 때
def walk(self):
    self.weight -= 0.5
    print("-외부- {}이 걸어서 {}kg가 됨".format(self.name, self.weight))

walk(person) # 외부함수 호출 - 인자 필요 : -외부- Tom이 걸어서 64.5kg가 됨
#walk() # 외부함수 호출 : Error

# 인스턴스 메소드 호출과 첫번째 매개변수 self
person.walk() # person 인스턴스의 walk호출 : -내부- Tom이 걸어서 64.5kg가 됨
#person이라는 인스턴스가 walk(self)의 첫번째 매개변수인 self에 자동으로 전달되기 때문 : 인스턴스인 첫번째는 self는 생략하고 전달

# self 외의 함수가 있을 때
person.speak('hello') #self 생략하고 하나만 넘겨주면 됨, 인스턴스가 자동으로 self로 전달됨 : hello



'''
메소드(Method)
 - 메소드는 함수와 비슷하다
 - 클래스에 묶여서 클래스와 인스턴스와 관계되는 일을 하는 함수를 말한다

함수 : 기능의 함수
메소드 : 클래스와 인스턴스의 함수
인가..?
'''



'''
메소드 이해하기

메소드(Method)
 - 메소드는 함수와 비슷하다.
 - 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수

클래스 내부에 함수를 포함시킨 예

    class Human( ):
        ''인간''
        def create( name, weight ): # 다음 강의에서 자세히 설명
            person = Human()
            person.name = name
            person.weight = weight
            return person

        def eat( self ):
            self.weight += 0.1
            print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

        def walk( self ):
            self.weight -= 0.1
            print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

    person = Human.create("철수", 60.5)
    person.eat()
    
self
 - 메소드의 첫번째 인자
 - 인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달

'''