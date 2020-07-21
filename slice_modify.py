# slice로 리스트 수정하기

numbers = [0,1,2,3,4,5,6,7,8,9]
numbers = list(range(10))
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del numbers[0]
print(numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:5]) #[1, 2, 3, 4, 5]

# 영역지정 삭제
del numbers[:5]
print(numbers) #[6, 7, 8, 9]

# 영역지정 수정
print(numbers[1:3]) #[7, 8]
numbers[1:3] = [77, 88]
print(numbers) #[6, 77, 88, 9]
numbers[1:3] = [77, 88, 99]
print(numbers) #[6, 77, 88, 99, 9]

numbers[1:4] = 8 #TypeError
numbers[1:4] = [8] 
print(numbers) #[6, 8, 9]


'''
Slice로 리스트 수정하기

slice 활용
 - 삭제
    del list[ :5 ] : 처음부터 5번째까지 삭제

 - 수정
    list[ 1:3 ] = [ 77, 88 ]
    list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환
    list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환
'''