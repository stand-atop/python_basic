
# 단순 오버라이드

class Animal():

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는댜")
        
    def greet(self):
        print("인사한다")

class Human(Animal):
    
    def wave(self):
        print("손을 흔든다")
        
class Dog(Animal):
    
    def wag(self):
        print("꼬리를 흔든다")
        
person = Human() # Human 객체생성
person.greet() #인사한다

dog = Dog() # Dog 객체생성
dog.greet() #인시한다



class Animal():

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는댜")
        
    def greet(self):
        print("인사한다")

class Human(Animal):
    
    def wave(self):
        print("손을 흔든다")
    
    # override로 greet()를 새로운 것으로 변경함
    def greet(self):
        self.wave()
        
class Dog(Animal):
    
    def wag(self):
        print("꼬리를 흔든다")
    
    # override로 greet()를 새로운 것으로 변경함    
    def greet(self):
        self.wag()
        
person = Human() # Human 객체생성
person.greet() #손을 흔든다

dog = Dog() # Dog 객체생성
dog.greet() #꼬리를 흔든다


class Cow(Animal):
    '''소'''

cow = Cow()
cow.greet() # 인사한다 - 단순 override로 변경하지 않고 사용



'''
단순 오버라이드

오버라이드(Override)
 - 같은 이름을 가진 메소드를 덮어 쓴다는 의미
 
    class Animal( ):
        def greet( self ):
            print( "인사한다" )

    class Human( Animal ):
        def greet( self ):
            print( "손을 흔든다" )

    class Dog( Animal ):
        def greet( self ):
            print( "꼬리를 흔든다" )
        
'''