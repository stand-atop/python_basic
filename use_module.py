# 모듈의 사용 : my_module

import my_module

# print(my_module.random_rsp())

selected = my_module.random_rsp()
print(selected)
print('가위?', my_module.SCISSOR == selected) #T or F


'''
모율을 직접 만들어서 사용할 수 있음
    파이썬 제공 모듈과 달리 직접 만든 모듈은 사용할 모듈과 작성한 모율이 같은 폴더 안에 들어있어야함
'''


'''
모듈 만들기

모듈 만들기
 - 사용할 함수, 메소드 코드를 작성한 모듈 파일을 생성
 - 모듈이 쓰일 파일에 import를 사용하여 모듈을 호출
 - 사용 방법은 기존의 모듈과 동일
 - 주의할 점은 사용자가 만든 모듈과 모듈을 쓸 파일이 같은 폴더에 있어야 한다.
'''
