#막대 그래프 그리기 과제

import csv
import matplotlib.pyplot as plt


file_path = "test.csv"

# 그래프 출력 리스트
dates = []
temps = []

## 파일을 읽을 때
## with open(파일명, mode='어떤모드로 읽을지', encoding='인코딩') as 객체명:
## 불러올 때는 with, 작성할 때는 write
with open(file_path, mode='r') as file : 

    reader = csv.reader(file)
    
    # 첫 줄을 읽어버리고
    # next 함수로 첫 줄을 읽음
    next(reader)    # header 값을 읽음
    
    ## for i in 객체 또는 배열 (향상된 for문)
    ## reader 안에 있는 것을 한 줄 씩 불러줘
    for row in reader :
    
        ## 일시가 12월인 값만 출력하고 싶어
        if row[2].startswith("Dec"):
            print(row[2].strip('Dec-'), row[-2])
            dates.append(row[2].strip('Dec-'))
            # str 타입이면 그래프 표시 때 숫자 크기별 순서대로 되지 않기 때문에
            # float 형으로 변경해줌
            temps.append(float(row[-2]))
         
# 출력할 데이터의 가로, 세로 길이 설정
plt.figure(figsize=(10,5))

# 막대 그래프는 plt.bar을 사용
plt.bar(dates, temps)

# 타이틀
plt.title("Temperature in Decenber")

# 출 라벨
plt.xlabel("Date", fontsize = 10)
plt.ylabel("Temperature", fontsize = 10)

# 그린 그래프를 화면에 출력해줘  =>  plt.show()
# 2개가 한 세트
plt.show


            