# 키(정수 값)가 담긴 배열과 키(정수 값) 값을 받음
# 받은 키 값보다 큰 값의 수를 반환

def solution(array, height):
    # 반환할 결과 변수
    # result = 0
    
    # # 배열 값을 차례로 가져와서 비교
    # # 배열만큼 반복
    # for i in array:
    #     # 키 비교 후 크면 개수 증가
    #     if(height < i):
    #         result = result + 1
    # return result
    
    # 다른 풀이
    # 키 값을 키 배열에 추가
    array.append(height)
    # 리스트를 내림차순으로 정렬한다.
    array.sort(reverse=True)
    # height의 인덱스 값은 내림차순으로 정렬했을 때
    # hight 보다 큰 수의 개수와 같으므로 해당 인덱스 값을 반환한다.
    return array.index(height)

# 결과 확인
array = [149, 180, 192, 170]
height = 160
print(solution(array, height))
array = [180, 120, 140]
height = 190
print(solution(array, height))
