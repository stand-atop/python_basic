
# 상속

class Human():

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
    def wave(self):
        print("손을 흔든다")
        

class Dog():
    
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
    def wag(self):
        print("꼬리를 흔든다")
        
person = Human() # Human 객체생성
person.walk() #걷는다
person.eat() #먹는다
person.wave() #손을 흔든다

dog = Dog() # Dog 객체생성
dog.walk() #걷는다
dog.eat() #먹는다
dog.wag() #꼬리를 흔든다
'''
walk(), eat() 코드가 중복됨
'''

# 중복코드 상속하기

class Animal():

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는댜")

class Human(Animal):
    
    def wave(self):
        print("손을 흔든다")
        
class Dog(Animal):
    
    def wag(self):
        print("꼬리를 흔든다")
        
person = Human() # Human 객체생성
person.walk() #걷는다
person.eat() #먹는다
person.wave() #손을 흔든다

dog = Dog() # Dog 객체생성
dog.walk() #걷는다
dog.eat() #먹는다
dog.wag() #꼬리를 흔든다

'''
상속하기 전과 후가 같은 결과 출력
'''




'''
상속

상속(Inheritance)
 - 상속하는 클래스를 부모 클래스
 - 상속받는 클래스를 자식 클래스
 - 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것

    class Animal( ):
        def walk( self ):
            print( "걷는다" )

        def eat( self ):
            print( "먹는다" )

    class Human( Animal ):
        def wave( self ):
            print( "손을 흔든다" )

    class Dog( Animal ):
        def wag( self ):
            print( "꼬리를 흔든다" )

'''