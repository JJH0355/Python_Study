#데이터의 시각화

import csv
# 별칭 설정
# 스크립트 기반의 코드들이 별칭 설정을 사용한다.
# matplotlib은 다양한 수학적인 연산, 정교한 그래프 등이 있다.
# matplotlib 라이브러리 안에 있는 pyplot 모듈을 사용
import matplotlib.pyplot as plt
# pip install matplotlib
# Python이 제공하는 라이브러리가 아니므로 따로 설치해야 함


## 파이썬은 '_'를 많이 사용함
file_path = "test.csv"

# 그래프 출력 리스트
dates = []
temps = []

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
    
        ## 일시가 12월인 값만 출력하고 싶어
        if row[2].startswith("Dec"):
            print(row[2], row[-2])
            dates.append(row[2])
            # str 타입이면 그래프 표시 때 숫자 크기별 순서대로 되지 않기 때문에
            # float 형으로 변경해줌
            temps.append(float(row[-2]))
         

# 그래프를 그리고  => plt.plot(x축 데이터, y축 데이터)
# 들어가는 인자는 리스트
plt.plot(dates, temps, marker='o', color='b', linestyle=':')

# 타이틀
plt.title("Temperature in Decenber")

# 출 라벨
plt.xlabel("Date", fontsize = 10)
plt.ylabel("Temperature", fontsize = 10)

# 그린 그래프를 화면에 출력해줘  =>  plt.show()
# 2개가 한 세트
plt.show


            