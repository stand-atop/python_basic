
# timedelta

import datetime
hundred = datetime.timedelta(days = 100)
print(type(hundred)) #<class 'datetime.timedelta'>

print(datetime.datetime.now() + hundred) #datetime.datetime(2020, 11, 1, 12, 9, 25, 676968)
print(type(datetime.datetime.now())) #<class 'datetime.datetime'>

# datetime클래스와 timedelta클래스의 계산
hundred_before = datetime.timedelta(days = -100)
print(datetime.datetime.now() + hundred_before) #2020-04-15 12:16:38.274588
print(datetime.datetime.now() - hundred) #2020-04-15 12:16:38.422933 - 위와 같은 값

# 오늘 9시부터 하루 뒤 날짜와 시간 계산
tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=1)
print(tomorrow) #2020-07-25 09:00:00.103058


'''
timedelta

timedelta 클래스
 - 시간의 연산을 가능하게 해주는 클래스
'''