
for i in range(5):
    print(i) #0 1 2 3 4

# 단순 반복과 대입
names = ['철수', '영희', '바둑이', '깜둥이']
for i in range(4):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))

# len() : 개수만큼 반복 대입    
names = ['철수', '영희', '바둑이', '깜둥이', '흰둥이']
for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))
    
# enumerate : 한번에 순서와 리스트 안의 값을 모두 만들어냄
for i, name in enumerate(names): 
    print('{}번: {}'.format(i + 1, name))
    

# range로 한글 출력
for i in range(11172):
    print(chr(44032 + i), end='')
    
    
'''
for in list : 순회할 리스트가 정해져 있을 때
for in range() : 순회할 횟수가 정해져 있을 때
'''


'''
for in range

range 함수
 - 필요한 만큼의 숫자를 만들어내는 유용한 기능

    for i in range(5):
        print(i)

enumerate
 - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
 
    names = ['철수', '영희', '영수']
    for i, name in enumerate(names):
        print('{}번: {}'.format(i + 1, name))
'''