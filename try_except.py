# try except : 예외처리/에러처리
'''
# IndexError
list = []
list[0] 

# ValueError
text = 'abc'
nmber = int(text)
'''

text = '100%'
try:
    number = int(text)
except ValueError: # 발생할 것 같은 에러코드 작성
    print('{}는 숫자가 아님'.format(text))
    

def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없음.'.format(index))

safe_pop_print([1,2,3],5) #5 index의 값을 가져올 수 없음


# if문을 대신 사용할 수 있음
def safe_pop_print_if(list,index):
    if index<len(list):
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올 수 없음.'.format(index))
safe_pop_print_if([1,2,3],5)
'''
try_except와 if문 중 간경한 코드를 사용하면 됨
간단한 경우는 if문 사용
try_except 만이 오류를 처리할 수 있는 경우도 있음
'''

'''
예외처리
    try:
       에러가 발생할 가능성이 있는 코드를
    except 에러 종류:
       에러가 발생 했을 경우 처리할 코드
        
예외처리 대신 if else를 사용할 수 있음
'''


'''
try except

예외 처리
    try:
        # 에러가 발생할 가능성이 있는 코드
    except Exception: # 에러 종류
        #에러가 발생 했을 경우 처리할 코드
        
 - 경우에 따라 예외 처리 대신 if else를 사용 할 수 있다.
'''