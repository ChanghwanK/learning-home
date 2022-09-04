# def solution(n):
#     answer = 0
#     str_n = str(n)
    
#     for num in str_n:
#       answer += int(num)
    

#     return answer
  
  
# print(solution(987))



### no-2

from turtle import st


def solution(n):
    str_n = str(n)
    answer = []
    for num in reversed(str_n):
      answer.append(int(num))
    
    return answer
  

print(solution(12345))