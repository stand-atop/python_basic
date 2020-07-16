
def get_web(url):
    '''URL을 넣으면 페이지 내용을 돌려주는 함수'''
    import urllib.request # urllib 라이브러리를 가져옴
    response = urllib.request.urlopen(url) # 받은 url을 염
    data = response.read() # 데이터를 읽고
    decoded = data.decode('UTF-8') # 사람이 읽을 수 있도록 디코딩함
    return decoded # 결과를 돌려줌


url = input('웹 페이지 주소는?') # http://example.com/
content = get_web(url)
print(content)

# content 결과값
'''
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
'''




'''
모율
 - 미리 만들어진 코드를 가져와 쓰는 방법
 - import <모듈이름>
 - 사용: <모듈이름>.<모듈안의 구성요소>
   + 예 :
        math.pi
        random.choice()
'''




'''
모듈 사용하기

모듈
 - 미리 만들어진 코드를 가져와 쓰는 방법
 - import 모듈이름
 - 사용 방법: 모듈이름.모듈안의 구성요소

    math.pi
    random.choice()

모듈의 예
 - import math
   + 수학과 관련된 기능
 - import random
   + 무작위와 관련된 기능
 - import urllib.request
   + 인터넷의 내용을 가져오는 기능
'''