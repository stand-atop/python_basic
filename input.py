# 사용자 입력 받기

mine = input()
print('mine:', mine) #입력값이 출력됨 : 가위 -> 가위

# input() : 사용자의 키보드 입력을 return
# round() : 수의 반올림 값을 return


print('가위 바위 보 가운데 하나를 내 주세요>', end = '')
mine = input()
pirnt('mine:', mine)


mine = input('가위 바위 보 가운데 하나를 내 주세요>')
pirnt('mine:', mine)


'''
input
 - 사용자 입력을 받는 방법
 - input('text') == print('text', end='')
                    input()
 - 파이썬이 제공하는 함수
 
 * ctrl + C = 프로그램 강제 종료
'''



'''
사용자 입력 받기

프로그래밍의 3단계
 - 사용자 입력
 - 자료 처리
 - 결과 출력

input()
 - 사용자의 키보드 입력을 return

    print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
    mine = input()
    print('mine:', mine)

 - 간단한 print기능을 내장

    mine = input('가위 바위 보 중 하나를 내주세요> ')
    print('mine:', mine)

Ctrl + c
 - 프로그램 즉시 종료
'''