# 인사 로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# old way
print(number, '번 손님', greeting, '.', place,
    '에 오신 것을', welcome, '!') # 20 번 손님 안녕하세요 . 문자열 포맷의 세계 에 오신 것을 환영합니다 !
    
# new way
base = '{}번 손님, {}.{}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome) # base.format : base에 속해있는 format

print(base) # {}번 손님, {}.{}에 오신 것을 {}!
print(new_way) # 20번 손님, 안녕하세요.문자열 포맷의 세계에 오신 것을 환영합니다!


# 가위바위보 예제 - format 활용
mine = '가위'
yours = '바위'
result = '졌다'

print('나는 {}, 너는 {}, 그래서 {}'.format(mine, yours, result))
'''
괄호의 개수가 맞을 때는 에러가 나지 않음
괄호의 개수가 맞지 않을 때도 에러가 나지 않을 수 있음
#print('나는 {}, 너는{}, 그래서'.format(mine,yours,result)
-> {}는 2개, format의 괄호 안에 든 변수는 3개 : 에러가 발생하지 않음.
#print('나는 {}, 너는 {}, 그래서{}{}'.format(mine,yours,result)
-> {}는 4개, format의 괄호 안에 든 변수는 3개 : 에러가 발생함.
'''



'''
format
문자열.format()
 - 문자열의 대괄호 자리에 format 뒤의 괄호안에 들어있는 값을 하나씩 넣는다
 - 문자열에 포함된 대괄호 개수 보다 format안에 들어 있는 값의 수가 많으면 정상 동작
   - print('{} 번 손님'.format(number,greeting))
 - 문자열에 포함된 대괄호 개수 보다 format안에 들어 있는 값의 수가 적으면 에러
   - print('{} 번 손님 {}'.format(number))


number = 20
welcome = '환영합니다'
base = '{} 번 손님 {}'

#아래 3개의 print는 같은 값을 출력
print(number,'번 손님',welcome)
print(base.format(number,welcome))
print('{} 번 손님 {}'.format(number,welcome))
#=>20 번 손님 환영합니다
'''