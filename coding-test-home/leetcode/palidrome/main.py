# palindrome
# 앞으로 읽어도 뒤로 읽어도 똑같은 것 ex) 1 2 2 1
import collections


def is_palindrome_list(datas):
  while(len(datas) > 1):
    if datas.pop(0) != datas.pop():
      return False
  
  return True


# print(is_palindrome_list([1,2,3,3,2,1])) 


def is_palindrome_list_deque(datas):
  deque = collections.deque()
  
  for data in datas:
    deque.append(data)
  
  while (len(deque) > 1):
    if deque.popleft() != deque.pop():
      return False
  
  return True
  

print(is_palindrome_list_deque([1,2,3,3,2,1])) 
