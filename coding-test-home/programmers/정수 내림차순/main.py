def solution(s):
    answer = ""
    num_list = list()
    
    for num in str(s):
        num_list.append(num)
    
    sorted_list = sorted(num_list, reverse=True)
    
    return int(answer.join(sorted_list))
