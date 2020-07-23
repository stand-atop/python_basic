
# 내 예외 만들기

'''
value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise ValueError("가위바위보 중에 하나의 값이어야 합니다.")

except ValueError: 
    print("에러발생")
    
'''
# 단순 ValueError는 다른 곳에서 나오는 에러와 중복될 수 있음

# 내 예외 사용하기 위해 선언
from UnexpectedRSPValue import UnexpectedRSPValue

value = '가'

try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")
    
# 내가 정의한 에러만 잡아 다른 에러와 헷갈리지 않을 수 있음


# 내 예외 사용하기 위한 예제
from UnexpectedRSPValue import BadUserName
from UnexpectedRSPValue import PasswordNotMatched

def sing_up():
    '''회원가입 함수'''

try:
    sign_up()
except BadUserName:
    print("이름으로 사용할 수 없는 입력입니다.")
except PasswordNotMatched:
    print("입력한 패스워드가 일치하지 않습니다.")

'''    
BadUserName, PasswordNotMatched를 UnexpectedRSPValue처럼 따로 파일을 만들어 예외를 분기 처리 할 수 있음
결국 제약사항 같은 걸 말하는 듯
'''


'''
사용자 정의 Exception
 - 사용자가 직접 예외처리를 하여 코드의 직관성을 높일 수 있다
 - Exception 클래스를 상속받아 만든다
'''


'''
내 예외 만들기

예외 정의
 - 사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
 - 파일을 하나 만들어 예외를 정의
 - Exception 클래스를 상속받아 만든다
 
    try:
        sign_up( )
    except BadUserName:
        print( "이름으로 사용할 수 없는 입력" )
    except PasswordNotMatched:
        print( "입력한 패스워드 불일치")
'''