# List와 문자열

my_list = [1,2,3,4,5,6]
print(my_list[0]) #1
print(my_list[1]) #2

str = "Hello Python"
print(str[0]) #'H'
print(str[1]) #'e'

print(3 in my_list) #True
print(9 in my_list) #False

print("H" in str) #True
print("z" in str) #False

print(my_list.index(5)) #4
print(str.index("t")) #8

characters = list("abcdef")
print(characters) #['a', 'b', 'c', 'd', 'e', 'f']

# 문자열 분할
words = "Python은 프로그래밍을 배우기 아주 좋은 언어입니다."
words_list = words.split()
print(words_list) #['Python은', '프로그래밍을', '배우기', '아주', '좋은', '언어입니다.']

time_str = "11:51:47"
time_list = time_str.split(":")
print(time_list) #['11', '51', '47']

# 문자열 병합
":".join(time_list) #'11:51:47'
" ".join(words_list) #'Python은 프로그래밍을 배우기 아주 좋은 언어입니다.'


'''
List와 String
 - 리스트와 문자열은 유사하다.
 - 서로 변환이 가능하다.
 - 문자열에서 리스트 ex)list=str.split()
 - 리스트에서 문자열 ex)" ".join(list)
'''
