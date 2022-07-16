
# 재귀 종료 조건 
# sort된 리스트에서 값을 찾는 것 
# _summary_
# 찾은 경우 (길이가 1인데 찾는 데이터인 경우)
# 길이가 1인데 데이터가 아닌 경우
# data 길이가 0인 경우 

data = [1,2,3,4,5,6,7]

def binary_search(data, search_num):    
    if len(data) == 1 and data[0] != search_num:
        print("Not Found")
        return False
    
    if len(data) == 1 and data[0] == search_num:
        return True
    
    if (len(data) == 0):
        return False
    
    mid = len(data) // 2
    
    if data[mid] == search_num:
        return True
    else:
        if data[mid] < search_num:
            return binary_search(data[mid:], search_num)
        else:
            return binary_search(data[:mid], search_num)
        
    
    
print(binary_search(data, 8))








