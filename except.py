# 예외의 이름을 모를 때
'''
list = []
print(list[0]) # error

text = 'abc'
number = int(text)
'''


try :
    list = []
    print(list[0])
except : # 에러 이름을 모를 때 한꺼번에 처리
    print('에러 발생')
    
    
    
try :
    #list = []
    #print(list[0])
    
    text = 'abc'
    number = int(text)
except Exception as ex : # 발생한 이름을 알고 싶을 때
    print('에러 발생',ex) # 에러 출력
    

'''
예외의 이름을 모를 때

예외 이름을 모르는 경우 처리 방법

    try:
        # 에러가 발생할 가능성이 있는 코드
    except Exception as ex: # 에러 종류
        print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수
'''