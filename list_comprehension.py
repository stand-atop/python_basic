
# List comprehension - 원하는 구성요소를 가지는 리스트를 만듬

# 길이가 1~10까지인 정사각형의 넓이를 요소로 가지는 리스트
# 기존 for문
areas = []
for i in range(1,11):
    areas = areas + [i*i]
print("areas : ", areas) #areas :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension
areas2 = [ i*i for i in range(1,11)] # [리스트에 넣기 원하는 계산식 + for문]
print("areas2 : ", areas2) #areas2 :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 특정 조건에서 만족하는 i만 가지고 리스트를 만들고 싶을 때 
# 기존 for문
areas = []
for i in range(1,11):
    if i%2 == 0: # 길이가 짝수일 때만
        areas = areas + [i*i]
print("areas : ", areas)

# List comprehension
areas2 = [ i*i for i in range(1,11) if i%2 == 0 ] # [리스트에 넣기 원하는 계산식 + for문 + 조건]
print("areas2 : ", areas2)


# List comprehension의 for문 중첩
# 길이가 15*15인 바둑판의 각 좌표를 튜블로 만들어 값으로 가지는 리스트
[(x,y) for x in range(15) for y in range(15)]
'''
[(0, 0), (0, 1), ... (0, 13), (0, 14), 
(1, 0), (1, 1), ... (14, 13), (14, 14)]
'''



'''
List

List Comprehension
 - 파이썬의 유용한 도
 
    예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
    예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
    예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]

'''