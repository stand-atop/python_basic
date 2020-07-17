
# 딕셔너리 : keys&values
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}
print(wintable['가위']) #보

# 리스트와 비슷함
words = ['a', 'b', 'c']
print(words[1]) #b


# 딕셔너리 활용
def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp('가위', '바위')
print(result) #lose


messages = {
    'win' : '이김',
    'draw' : '쌤쌤',
    'lose' : '졌음'
}
print(messages[result]) #졌음



'''
dictionary
 - 여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
 - 이름표를 이용하여 값을 꺼내 사용
 - 딕셔너리명 = {
       '이름표1' : '값1',
       '이름표2' : '값2'
   }
'''


'''
딕셔너리 만들기

딕셔너리
 - 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
 - 이름표를 이용하여 값을 꺼내 사용
 - 사용할 때는 리스트와 비슷한 방식

        wintable = {
            '가위' : '보',
            '바위' : '가위',
            '보' : '바위',
        }
        print(wintable['가위'])
'''