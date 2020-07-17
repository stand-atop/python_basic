
# 딕셔너리 반복문

# 리스트 반복문
seasons = ['봄', '여름', '가을', '겨울']
for season in seasons:
    print(season)
    
    
# 딕셔너리 반복문 : 경우에 따라 keys 나 values 값을 가져올 수 있음
ages = {
    'Tod' : 10,
    'Jane' : 20,
    'Paul' : 50
}
print(ages)

# 딕셔너리 valuse 출력 반복문
for value in ages.values():
    print(value)

# 딕셔너리 keys 출력 반복문 : key가 있어야 값을 가져올 수 있음
for key in ages.keys():
    print(key)
    print('{}의 나이는 {}입니다.'.format(key,ages[key]))
    
# 딕셔너리 keys를 자동 인식해서 우선 keys를 불러옴
for value in ages:
    print(value) #Tod Jane Paul
    
# keys와 values 값을 동시에 처리하고 싶을 때
for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key,value))

# 딕셔너리는 리스트와 달리 순서가 지켜지지 않음




'''
Dictionary 반복문
 - 이름표=key
 - for key in ages.keys(): #keys() 생략가능
       print(key)
 - for value in ages.values():
       print(value)
 - for key, value in ages.items():
       print(key,value)
 - 순서와 상관없이 for문 실행
'''



'''
딕셔너리와 반복문

딕셔너리 반복문 활용
 - 경우에 따라 가져올 값을 정할 수있다.

    for key in ages.keys(): # keys() 생략 가능
        print(key)
    for value in ages.values():
        print(value)

 - key와 value 둘다 가져올 수 있다.

    for key, value in ages.items():
        print('{}의 나이는 {} 입니다'.format(key, value))

 - 딕셔너리는 값의 순서를 지키지 않는다.
'''