def solution(order):
	## 결과 값을 담을 변수 생성
    result = 0
    
    ## 비교를 위해 문자열로 변경
    orderStr = str(order);

    ## 받은 입력 값을 한 글자씩 가져와서 3, 6, 9에 비교
    ## 만약 3 또는 6 또는 9이면 결과 값에 1추가
    ## 반복에는 입력받은 값의 길이라는 횟수 제한이 있음
    for i in orderStr:
        ## i번째 index 위치의 글자 하나 씩 가져오기
        if(i == '3' or i == '6' or i == '9') :
            result += 1

    return result;
    
## 함수 사용 부분
order = 3;
order2 = 29423;

print(solution(order))
print(solution(order2))