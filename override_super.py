
# super()

class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
    def greet(self):
        print("인사한다")
    
class Human(Animal):
    
    def wave(self):
        print("손을 흔들면서")
        
    # override
    def greet(self):
        self.wave() # greet()를 자기 것으로 재정의 하여 사용
        super().greet() # 상속받은 Animal의 greet()를 그대로 사용
        
person = Human()
person.greet() #손을 흔들면서 인사한다    


# 부모 __init__ 활용
class Animal():
    def __init__(self, name): # init으로 초기값 설정
        self.name = name

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
    def greet(self):
        print("{}가 인시한다.".format(self.name)) # init 활용
    
class Human(Animal):
    
    def wave(self):
        print("손을 흔들면서")
        
    # override
    def greet(self):
        self.wave() 
        super().greet() 
        
person = Human("동식이") # 부모 init에 입력할 변수
person.greet() #손을 흔들면서 동식이가 인사한다



# __init__ 활용
class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
    def greet(self):
        print("{}가 인시한다.".format(self.name))
    
class Human(Animal):

    def __init__(self, name, hand): # 자식 init설정
        super().__init__(name) # 부모 init 호출해 name 초기화
        self.hand = hand # hand 초기화
    
    def wave(self):
        print("{}손을 흔들면서".format(self.hand )) # 스스로의 init 활용
        
    # override
    def greet(self):
        self.wave()
        super().greet()
        
person = Human("동식이", "오른") # init에 넣을 변수 .. init 실행 순서는...??
person.greet() #오른손을 흔들면서 동식이가 인사한다


'''
super()

super()
 - 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
 - super().부모클래스내용
 
    class Animal( ):
        def __init__( self, name ):
            self.name = name

    class Human( Animal ):
        def __init__( self, name, hand ):
            super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
            self.hand = hand

    person = Human( "사람", "오른손" )

'''