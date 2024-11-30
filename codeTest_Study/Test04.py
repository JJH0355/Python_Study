# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
def solution(n):
    # 결과 값을 구할 변수 생성
    result = 0
    
    # n 이하의 수를 반복
    # n도 포함되어야 함
    for i in range(n+1):
        # 만약 짝수면 기존 값에 더하고
        if i%2 == 0 :
            result = result + i
        # 아니면 그대로 통과
    return result

# 실행
print(solution(10))
print(solution(4))
