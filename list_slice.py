# slice

list = [1, 2, 3, 4, 5]
print(list[1]) #2

text = "Hello Python"
print(text[1]) #e

print(text[1:5]) #'ello'

list = ['영구','땡칠이','삼식이','말숙이','춘식이']
print(list[1:3]) #['땡칠이', '삼식이']
print(list[0:2]) #['영구', '땡칠이']

print(list[2:len(list)]) #['삼식이', '말숙이', '춘식이']

print(list[2]) #삼식이

# 처음~
print(list[:2]) #['영구', '땡칠이']
print(list[0:2]) #['영구', '땡칠이']

# ~끝
print(list[2:len(list)]) #['삼식이', '말숙이', '춘식이']
print(list[2:]) #['삼식이', '말숙이', '춘식이']

# 전체
print(list[:]) #['영구', '땡칠이', '삼식이', '말숙이', '춘식이']
print(list) #['영구', '땡칠이', '삼식이', '말숙이', '춘식이']

# 슬라이스된 리스트 비교
list1 = [1,2,3,4,5]
list2 = list1[:]

print(list1) #[1, 2, 3, 4, 5]
print(list2) #[1, 2, 3, 4, 5]

list1.reverse()
print(list1) #[5, 4, 3, 2, 1]
print(list2) #[1, 2, 3, 4, 5]


'''
Slice

slicing
 - 리스트나 문자열에서 값을 여러개 가져오는 기능

    text = "hello world"
    text = text[ 1:5 ]
    list = [ 0, 1, 2, 3, 4, 5 ]
    list = list[ 1:3 ]

 - slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.
 - 시작과 끝부분을 얻어 오는 방법

    list[ 2: ] : 2번째부터 끝까지 반환
    list[ : 2 ] : 처음부터 2번째 까지 반환
    list[ : ] : 처음부터 끝까지 전부 반환
'''