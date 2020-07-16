
# 모듈 만들기 : 가위바위보

def random_rsp():
    '''무작위 가위바위보'''
    import random
    return random.choice(['가위', '바위', '보'])
    

# 변수

PAPER = '보'
SCISSOR = '가위'
ROCK = '바위'