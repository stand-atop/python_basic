
# 모델링

class Human():
    '''사람'''

# 일반 클래스 사용
#person = Human()
#person.name = '철수'
#person.weight = 76

# 함수 사용
def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person
person = create_human('철수', 76) # 함수로 사람이 만들어짐

# 클래스에 함수 넣기
Human.create = create_human
person = Human.create('철수', 76) # 클래스와 함수로 사람이 만들어짐

# 먹기
def eat(person):
    person.weight += 0.5
    print("{}가 먹어서 {}kg이 됨".format(person.name, person.weight))
    
# 걷기
def walk(person):
    person.weight -= 0.5
    print("{}가 걸어서 {}kg이 됨".format(person.name, person.weight))
    
Human.eat = eat
Human.walk = walk

person.walk() #철수가 걸어서 75.5kg이 됨
person.eat() #철수가 먹어서 76.0kg이 됨
person.eat() #철수가 먹어서 76.5kg이 됨



'''
모델링
모델링(modeling)
 - 클래스로 현실의 개념을 표현하는 것
'''