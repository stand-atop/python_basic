
# Dictionary

students = ['태연', '진우', '정현', '하늘', '성진']

for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number, name))
'''
0번의 이름은 태연입니다.
1번의 이름은 진우입니다.
2번의 이름은 정현입니다.
3번의 이름은 하늘입니다.
4번의 이름은 성진입니다.
'''

# dictionary comprehension
students_dict = {"{}번".format(number +1): name for number, name in enumerate(students)} #{ 키 : for문 }
print(students_dict) #{'1번': '태연', '2번': '진우', '3번': '정현', '4번': '하늘', '5번': '성진'}

# zip : 두 개 이상의 리스트나 string을 받아 index에 맞게 for문에서 하나씩 출력할 수 있게 만들어 주는 역할
scores = [87, 97, 79, 89, 100]
for x, y in zip(students, scores):
    print(x,y)
'''
태연 78
진우 99
정현 80
하늘 90
성진 100
'''

# dictionary comprehension 으로 zip 활용
score_dic = {student : score for student, score in zip(students, scores)}
print(score_dic) #{'태연': 87, '진우': 97, '정현': 79, '하늘': 89, '성진': 100}

'''
Comprehension 예시

List Comprehension

 - [ 계산식 for문 ]
    [ i*i for i in range(1,11)]
    
 - [ 계산식 for문 조건문 ]
    [ i*i for i in range(1,11) if i%2 == 0]
    
 - [ 형식 for문 for문 ]
    [ (x,y) for x in range(15) for y in range(15)]


Dictionary Comprehension

 - { 형식 : for문 }
    {"{}번".format(number) : name for number, name in enumerate(students)}

'''



'''
Dictionary

Dictionary Comprehension
 - 파이썬의 유용한 도구
 - 예시
    { "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]
    {student:score for student, score in zip(students, scores)}
'''