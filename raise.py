# 에러 강제 발생시키기

def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
        
#rsp('가위','바') # valueError

'''
try :
    rsp('가위', '바')
except ValueError :
    print('잘못된 값을 넣음')
'''


school = {'1반':[166, 170, 154, 148, 173, 160], '2반':[165, 178, 159, 162, 175, 167]}
for class_number, students in school.items() :
    for student in students :
        if student > 170 :
            print(class_number,'에 170을 넘는 학생이 있음')
            break # 내부 for문 정지, 외부 for문 실행
'''
1반 에 170을 넘는 학생이 있음
2반 에 170을 넘는 학생이 있음
'''

try:
    for class_number, students in school.items():
        for student in students:
            if student > 170 :
                print(class_number,'에 170을 넘은 학생있음')
                raise StopIteration  #에러 발생시킴 : 내외부 for문 모두 정지
except StopIteration:
    print('정상종료')
'''
1반 에 170을 넘은 학생있음
정상종료
'''



'''
예외 발생 시키기

try:
    ..
    raise 에러 종류 # 에러 발생 시킬 위치
    ..
exception 에러종류:
    처리할 코드

 - 많이 사용하면 코드 읽기 어려워짐
 '''
 
 
 '''
raise

예외 발생
 - 사용자가 직접 에러를 발생시키는 기능
 - raise Exception # 에러 종류
 - 많이 사용하면 코드를 읽기 어려워진다.
'''