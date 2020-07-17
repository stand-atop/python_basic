# 딕셔너리와 리스트의 비교

# 공통점
# 입력
list = [1,2,3,4,5]
dict = {
    'one' : 1,
    'two' : 2
}

# 선택 출력
print(list[0])
print(dict['one'])

# 선택 삭제
del list[0]
print(list)
del dict['one']
print(dict)

# 개수 확인
len(list)
print(list)
len(dict)
print(dict)

# 값 확인
2 in list # list에 2가 있는지 확인 = True
7 in list # list에 7이 있는지 확인 = False
'two' in dict.keys() # dict에 'two'keys가 있는지 확인 = True
'three' in dict.keys() # dict에 'three'keys가 있는지 확인 = False
2 in dict.values() # dict에 2 values가 있는지 확인 = True
3 in dict.values() # dict에 3 values가 있는지 확인 = False

# 모두 비우기
list.clear()
print(list)
dict.clear()
print(dict)




# 차이점
# 리스트는 keys가 없기 때문에 변경사항이 생기면 순서 출력 값이 변할 수 있음
list = [1,2,3,4,5]
dict = {
    'one' : 1,
    'two' : 2
}
list[2] #3 
print(list) #[1,2,3,4,5]
list.pop(0) # list의 0번째 값 삭제
list[2] #4
print(list) #[2,3,4,5]

# 딕셔너리는 keys를 가지고 values를 찾아가기 때문에 변경사항이 생겨도 호출에 따른 출력값이 변하지 않음 /values값 변경 예외
dict['two'] #2
dict.pop('one') # dict의 'one' keys를 가진 것을 삭제
dict['two'] #2


# 리스트의 추가는 값이 중복될 수 있다
# 리스트+리스트를 사용할 수 있다
big_list = [1,2,3]+[3,4,5,6]
print(big_list) #[1,2,3,3,4,5,6]

# 딕셔너리 + 딕셔너리는 update()함수를 사용하고,
# 딕셔너리의 keys값의 중복은 기준이 되는 기존 값이 변경되어(덮어쓰기) 중복되는 keys를 용인하지 않은는다.
dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}
dict1.update(dict2) # 기준이 되는 dict1에 dict2값을 추가한다
print(dict1) #{1:1000, 2:200, 3:300}
dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}
dict2.update(dict1) # 기준이 되는 dict2에 dict1값을 추가한다
print(dict2) #{1:100, 2:200, 3:300}



'''
리스트와 비교

 - 공통점
                    List	                            Dictionary
    생성  	    list = [ 1, 2 ,3 ]	            dict = { 'one':1, 'two':2 }
    호출	        list[ 0 ]	                    dict[ 'one' ]
    삭제	        del( list[ 0 ] )	            del( dict[ 'one' ] )
    개수 확인	    len( list )	                    len( dict )
    값 확인	    2 in list	                    'two' in dict.keys( )
    전부 삭제	    list.clear( )	                dict.clear( )

 - 차이점
                List	                                Dictionary
    순서	    삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다	key로 값을 가져오기 때문에 삭제 여부와 상관없다
    결합	    list1 + list2	                    dict1.update( dict2 )
'''