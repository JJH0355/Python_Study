def solution(numbers):
    ## 더한 수를 넣을 실수 변경
    total = 0.0
		
	## 배열의 길이를 계산해 놓음
    numberLength = len(numbers)
    
    ## 배열의 길이만큼 반복
    ## 배열의 안의 값을 차례로 더함
    

	## 배열의 길이만큼 반복
	## 배열의 안의 값을 차례로 더함
    for i in numbers :
        total += i
		
	## 모두 더한 값을 배열의 길이로 나눔
    result = total / numberLength
		
	## 결과 반환
    return result
    
## 함수 사용 부분
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(solution(numbers))