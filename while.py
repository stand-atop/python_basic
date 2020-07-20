
# while 반복문
# while 반복문 : 조건이 맞을 때까지 실행
selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
print('선택된 값은: ', selected)

# if 조건문 : 조건이 맞을 경우만 실행. 딱 1번
if selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
print('선택된 값은: ', selected)

# for 반복문 : 
patterns = ['가위', '바위', '보']
for pattern in patterns:
    print(pattern)

for i in range(len(patterns)):
    print(patterns[i])
    
'''
while 반복문은 for 반복문에 비해 length, i 등 새롭게 선언해주어야 할 요소가 더 있음
while 반복문을 사용하는 이유는 위의 가위바위보 예제처럼 어떤 값을 입력받을 때까지 
반복해야 하는 경우 등을 작성할 때 for 반복문 보다 간결함
'''
patterns = ['가위', '바위', '보']
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i = i + 1
    

'''
while문
 - if문은 조건이 맞으면 한번만 실행 하지만 while 반복문은 조건이 맞다면 계속 반복함
 - for 반복문으로 작성한 코드는 while 반복문으로도 작성 할 수 있음
 - 상황에 맞는 반복문을 사용하면 됨
'''



'''
while문 쓰기

while문
 - 조건이 참인 경우 계속 실행하는 반복문

    while selected not in ['가위', '바위', '보']:
        selected = input('가위, 바위, 보 중에 선택하세요>')
 
 - for 반복문으로 작성한 코드는 while 반복문으로 작성 할 수 있다.
'''