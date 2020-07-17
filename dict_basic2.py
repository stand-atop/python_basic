
# 딕셔너리 수정

# 리스트의 경우
#입력
list = [1,2,3,4,5]
print(list) #[1, 2, 3, 4, 5]

#수정
list[2] = 33
print(list) #[1, 2, 33, 4, 5]

#추가
#list[5] = 6 #error
print(list)  #[1, 2, 33, 4, 5]
list.append(6)
print(list) #[1, 2, 33, 4, 5, 6]

#삭제
del list[0]
print(list) #[2, 33, 4, 5, 6]
list.pop(0) #삭제하면서 출력 
print(list) #[33, 4, 5, 6]


# 입력
dict = {
    'one' : 1,
    'two' : 2
}
print(dict) #{'one': 1, 'two': 2}

# 수정
dict['one'] = 11
print(dict) #{'one': 11, 'two': 2}

# 추가
dict['three'] = 3
print(dict) #{'one': 11, 'two': 2, 'three': 3}

# 삭제
del dict['one']
print(dict) #{'two': 2, 'three': 3}
dict.pop('two') #삭제하면서 출력
print(dict) #{'three': 3}



'''
dictionary 수정하기
 - 값 수정
   + dict['one'] = 11
   
 - 값 추가
   + dict['three'] = 3

 - 값 삭제
   + del(dict['one'])
   + dict.pop('two')
'''
