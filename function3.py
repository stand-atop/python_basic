
def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    
    print('해는 {} 또는 {}'.format(r1,r2))

x = 1
y = 2
z = -8

# a * X^2 + b* X + c = 0, a != 0 인 X에 관한 2차방정식에 대해,
# 근의 공식은

print_root(x, y, z)

x = 2
y = -6
z = -8

# 한 번 더 구하려면

print_root(x, y, z)



def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.6)



'''
매개변수 : 함수를 정의할 때 사용하는 이름
실행 인자 : 함수를 실행할 때 넘기는 변수, 값
매개변수와 실행 인자
- 매개변수와 실행 인자의 개수는 동일해야 한다.
- 여러 개일 경우 쉼표로 구분


def print_round(number):    # 함수의 정의
    rounded = round(number)
    print(rounded)  

print_round(4.6)        # 함수의 호출
print_round(2.2)

'''