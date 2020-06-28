
def add_10(value):
    #value에 10을 더한 값을 돌려주는 함수
    if value < 10 :
        result = 10 # 즉시 종료
    else:
        result = value + 10
    return result
    
n = add_10(5)
print(n)
n = add_10(42)
print(n)

n = round(1.5)
print(n)


'''
함수의 return
-함수는 return을 이용해 값을 돌려줄 수 있다.
-함수를 사용하는 것은 함수 안의 코드를 모두 실행한 뒤 이 함수의 자리에 return에 있는 값을 넣은 것과 같다.
-여러 값을 반환하려면?
    return 뒤에 여러 값을 쉼표로 나누어 넣는다.
'''