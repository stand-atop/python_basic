# 논리 연산 더 알아보기

a = 10
if a < 10 and 2**a > 1000 and a % 5 == 2 and round(a) == a:
    print('복잡한 식') # != a
    

def return_false():
    print('return_false')
    return False

def return_true():
    print('return_true')
    return True

print('Test1')
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)
'''
Test1
return_false
return_true
False
'''
# 단락평가
print('Test2')
if return_false() and return_true():
    print('True')
else:
    print('False')
'''
Test2
return_false  # 단락평가 : 파이썬에서 조건식을 판별할 때 조건 앞 순서 부분에서 틀리면 뒷부분은 실행 자체를 하지 않음
False
'''

# 단락평가 예문
dic = {'Keys2':'Value1'}
if 'Key1' in dic and dic['Key1'] == 'Value1': # 조건 순서
    print('Key1도 있고, 그 값은 Value1이다')
else:
    print('아님')
#아님
    
dic = {'Keys2':'Value1'}
if dic['Key1'] == 'Value1' and 'Key1' in dic: # 조건 순서
    print('Key1도 있고, 그 값은 Value1이다')
else:
    print('아님')
#단락평가로 첫번째에서 에러



'''
논리연산 더 알아보기

단락평가
 - 논리연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정
 - 복잡한 코드를 단순하게 하는 방식
'''