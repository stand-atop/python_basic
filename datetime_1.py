
# Datetime

import datetime
print(datetime.datetime.now()) #datetime.datetime(2020, 7, 24, 11, 24, 10, 527599)

start_time = datetime.datetime.now()
print(type(start_time)) #<class 'datetime.datetime'> - datetime클래스에는 replace() 메소드가 있음

# 시간값의 변경 - replace()
start_time = start_time.replace(year=2009, month=2, day=1)
print(start_time) #datetime.datetime(2009, 2, 1, 11, 26, 12, 107965)

# 내가 원하는 시간값으로 만듬
start_time = datetime.datetime(2020,1,1)
print(start_time)

# 남은 시간 계산 - timedelta 클래스
start_time = datetime.datetime(2020,9,1)
how_long = start_time - datetime.datetime.now()
print(type(how_long)) #<class 'datetime.timedelta'> - timedelta클래스에 days와 seconds로 남은 시간을 계산할 수 있음
print(how_long.days) #38
print(how_long.seconds) #44498 - 초를 이용해 시간과 분을 계산해야함

print("9월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600)) #9월 1일까지는 38일 12시간이 남았습니다.


'''
datetime

datetime 모듈
 - 날짜와 시간을 사용하게 해주는 라이브러리

'''