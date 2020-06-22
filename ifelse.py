# if-else문
'''
if True :
    pass #조건이 참일 때 실행

else :
    pass #조건이 거짓일 때 실행
'''


scissor = "가위"
rock = "바위"
paper = "보"

win = "이김"
draw = "비김"
lose = "짐"

mine = "가위"
yours = "바위"

if mine == yours :
    result = draw
else :
    result = "이겼거나 졌거나"
print(result)


if mine == yours :
    result = draw
else :
    if mine == scissor :
        if yours == rock :
            result = lose
        else : 
            result = win
            
    else :
        if mine == rock :
            if yours == paper :
                result = lose
            else : 
                result = win
        else :
            if mine == paper :
                if yous == scissor :
                    result = lose
                else : 
                    result = win
            else :
                print("이상함")
print(result)


'''
else와 elif

if True:
    pass #조건이 참일 때 실행
elif False:
    pass #다른 조건이 참일 때 실행
else:
    pass #조건이 거짓일 때 실행
'''




if mine == yours :
    result = draw
else :
    if mine == scissor :
        if yours == rock :
            result = lose
        else : 
            result = win
            
    elif mine == rock :
        if yours == paper :
            result = lose
        else : 
            result = win
    elif mine == paper :
        if yous == scissor :
            result = lose
        else : 
            result = win
    else :
        print("이상함")
print(result)