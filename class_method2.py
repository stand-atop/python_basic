
# 특수한 메소드

class Human():
    '''사람'''
    
    def __init__(self, name, weight):
        '''초기화 함수'''
        #print("__init__실행 : 자동 호출되는 함수")
        #print("이름은 {}, 몸무게는 {}".format(name, weight))
        
        # create(name, weight) 대체
        self.name = name
        self.weight = weight
    
    def __str__(self):
        '''문자열화 함수'''
        return "{}(뭄무게 {}kg)".format(self.name, self.weight)
    
    ''' __init__의 매개변수를 활용해 대체함
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    '''
    def eat(self):
        person.weight += 0.5
        print("{}가 먹어서 {}kg이 됨".format(person.name, person.weight))
        
    def walk(self):
        person.weight -= 0.5
        print("{}가 먹어서 {}kg이 됨".format(person.name, person.weight)) 
        

# __init__ 메소드 : 클래스 호출 시 자동으로 실행 
# 매개변수가 없는 경우      
#person = Human() #__init__실행 : 자동 호출되는 함수

# 매개변수가 있는 경우
person = Human("홍식이", 66)

# __init__ 매개변수로 create 대체 확인
print(person.name) #홍식이
print(person.weight) #66

# __str__ 메소드 : 클래스를 string으로 표현할 때 표현 형식을 지정함
print(person) #인스턴스 자체 호출 시 : 홍식이(뭄무게 66kg)


'''
특수한 메소드

초기화 함수 : __init__
 - 인스턴스를 만들 때 실해오디는 함수

문자열화 함수 : __str__
 - 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수
'''


'''
특수한 메소드

초기화 함수
 - __init__ : 인스턴스를 만들 때 실행되는 함수

문자열화 함수
 - __str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수

    class Human( ):
        ''인간''
        def __init__( self, name, weight ):
            ''초기화 함수''
            self.name = name
            self.weight = weight

        def __str__( self )
            ''문자열화 함수''
            return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

    person = Human( "사람", 60.5 ) # 초기화 함수 사용
    print( person ) # 문자열화 함수 사용

'''