# list의 다양한 기능

list1 = [135, 462, 27, 2753, 234]
print(list1.index(27)) #2

#print(list1.index(50)) #ValueError

if 50 in list1:
    print(list1.index(50)) #에러안남

# list추가    
# list + list
list2 = [1,2,3] + [4,5,6]
print(list2) #[1,2,3,4,5,6]

# list.extend()
list1.extend([9,10,11])
print(list1) #[135, 462, 27, 2753, 234, 9, 10, 11]

# list.insert(index, value)
list1.insert(2,999)
print(list1) #[135, 462, 999, 27, 2753, 234, 9, 10, 11]

list1.insert(-1, 9999)
print(list1) #[135, 462, 999, 27, 2753, 234, 9, 10, 9999, 11]

# index값 초과 시 가장 마지막에 입력
list1.insert(10000,1000)
print(list1) #[135, 462, 999, 27, 2753, 234, 9, 10, 9999, 11, 1000]

# list 정렬
# list.sort() : 오름차순
list1.sort()
print(list1) #[9, 10, 11, 27, 135, 234, 462, 999, 1000, 2753, 9999]

#list.reverse()
list1.reverse()
print(list1) #[9999, 2753, 1000, 999, 462, 234, 135, 27, 11, 10, 9]



'''
List의 다양한 기능

List의 기능
 - list.index( value ) : 값을 이용하여 위치를 찾는 기능
 - list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
 - list.insert( index, value ) : 원하는 위치에 값을 추가
 - list.sort( ) : 값을 순서대로 정렬
 - list.reverse( ) : 값을 역순으로 정렬
'''