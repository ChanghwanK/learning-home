from typing import List


def merge_sort(datas: List[int]):
  # split 
  if len(datas) <= 1:
    return datas
  
  mid = len(datas) // 2
  
  left = merge_sort(datas[:mid])
  right = merge_sort(datas[mid:])
  
  return merge(left, right)


def merge(left: List[int], right: List[int]):
  merged = []
  left_point = right_point = 0
  
  while len(left) > left_point and len(right) > right_point:
    if left[left_point] > right[right_point]:
      merged.append(right[right_point])
      right_point += 1
    else:
      merged.append(left[left_point])
      left_point += 1
      
  while len(left) > left_point:
    merged.append(left[left_point])
    left_point += 1
  
  while len(right) > right_point:
    merged.append(right[right_point])
    right_point += 1
  
  return merged
    
  
  
    

print(merge_sort([1,4,2,3,6]))
