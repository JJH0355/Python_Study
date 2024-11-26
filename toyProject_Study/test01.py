## 3번째 일시 >> [2]
## 4번째 평균기온 >> [3]
## 최저 기운 >> [-2]

import csv

## 파이썬은 '_'를 많이 사용함
file_path = "test.csv"

## 파일을 읽을 때
## with open(파일명, mode='어떤모드로 읽을지', encoding='인코딩') as 객체명:
## 불러올 때는 with, 작성할 때는 write
with open(file_path, mode='r') as file : 
    # reader은 내장함수가 아니여서 import를 해야한다.
    # 자바에서는 패키지, 파이썬에서는 모듈
    reader = csv.reader(file)
    
    # 첫 줄을 읽어버리고
    # next 함수로 첫 줄을 읽음
    next(reader)    # header 값을 읽음
    
    ## for i in 객체 또는 배열 (향상된 for문)
    ## reader 안에 있는 것을 한 줄 씩 불러줘
    for row in reader :
    # print(row)
    #     ## print 한 번 당 리스트로 나옴
    #     ## row가 list 타입이라는 사실도 확인 가능
    #    print(row[2], row[3]) # row 가 list 타입이라는 사실도 확인가능!
    
        ## 일시가 12월인 값만 출력하고 싶어
        if row[2].startswith("Dec"):
            print(row[2], row[-2])
            
            
# 반복문 안에 로직코드가 한 번만 작동하는데 종료문이 아닐 때
# 밖에 있는게 유리
# 종료문은 안에 있는게 맞음


