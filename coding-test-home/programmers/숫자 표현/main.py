# 연속해야 함
# 합 == n이면 스탑
# 한 번 사용한 숫자도 사용 가능
# def solution(n):
#     nums = [] # callabo list
#     answer = 0
#     result = 0
    
#     for num in range(1, n+1): 
#         collabo = []
#         result += num 
        
#         if (result == n):
            
#         else:
#             collabo.append(num)    
        
#     return answer

# 완전 탐색을 하는 것임
# 완전 탐색을하고 조건을 찾는다. (일단 반복을 여러번 함 n^2 같은 케이스는 아니지만)
# 조건에 맞는 것들을 찾는다. 
# 조건 정의
# 1. 연속되는 숫자여야함
# 2. 합이 == n이면 멈춤
def solution(n):
    answer = 0
    # 이 방식은 지나간 숫자를 다시 넣을 수 없음 
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1): # i 부터야 함
            sum += j
            if sum == n:    
                answer += 1
                break
            if sum > n:
                break
    return answer

result = solution(15)
print(f"result >>> {result}")

def solution2(n):
    count = 0                      
    for i in range(1, n+1):         # 예시의 `15=15`도 있기 때문에 n+1 까지 반복문 실행
        sumN = 0                     
        for j in range(i, n+1):     # i값을 시작으로 반복문 실행
            sumN += j               # i값부터 계속해서 값을 더해준다
            if sumN == n:           # 더한 값이(sumN)이 n과 같다면 count +1, break
                count += 1          
                break
            if sumN > n:            # 더한 값(sumN)이 n보다 크다면 계산할 필요가 없음
                break
    return count

# print(solution2(15))