# tuple을 이용한 함수 return값

# list tuple
list = [1, 2, 3, 4, 5]
for index, value in enumerate(list):
    print('{}번째 값: {}'.format(index,value))

# tuple 이기 때문에 변수 하나로 처리 가능
for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0],a[1]))
    
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a)) #*a a tuple을 쪼갬


# dictionary tuple
ages = {
    'Tod' : 10,
    'Jane' : 28,
    'Paul' : 31
}
for key, value in ages.items():
    print('{}의 나이: {}'.format(key,value))

# tuple 이기 때문에 변수 하나로 처리 가능
for a in ages.items():
    print('{}의 나이: {}'.format(a[0], a[1]))

for a in ages.items():
    print('{}의 나이: {}'.format(*a))




'''
튜플을 이용한 함수의 리턴값

 - 튜플 리스트 활용

        for a in enumerate(list):
            print('{}번째 값: {}'.format(a[0], a[1]))

        for a in enumerate(list):
            print('{}번째 값: {}'.format(*a))

 - 튜플 딕셔너리 활용
 
        for a in dict.items():
            print('{}의 나이는:{}'.format(a[0], a[1]))

        for a in dict.items():
            print('{}의 나이는:{}'.format(*a))
'''