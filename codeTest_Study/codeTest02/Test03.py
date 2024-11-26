def solution(array, n):
    ## 결과를 담을 정수 변수
    result = 0
    
    ## 배열의 인덱스 0부터 인덱스 배열 길이 -1 까지의 값을 차례로 가져옴
    ## n과 값이 같은지 비교
    ## 만약 같다면 결과 값에 1 추가
    for i in array :
        if(i == n) :
            result += 1
            
    return result;
    
## 함수 사용 부분
numbers = [ 1, 1, 2, 3, 4, 5 ];
n = 1;
numbers2 = [ 0, 2, 3, 4 ];
n2 = 1;

print(solution(numbers, n))
print(solution(numbers2, n2))