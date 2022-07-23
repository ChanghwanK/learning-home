
from curses.ascii import isalnum
from collections import deque
from tkinter import W


def solution(s):
    answer = True
    strs = []
    for word in s:
        if isalnum(word):
            strs.append(word.lower())
            
    while len(strs) > 1:
        a = strs.pop(0)
        b = strs.pop()
        print("first => {a}")
        print("last => {b}")
        if a != b:
            answer = False
            return answer
    
    return answer

s = 'A man, a plan, a anal: Panama'
print(solution(s))


def solution(s):
    answer = True
    strs = deque()
    
    for word in s:
        if isalnum(word):
            strs.append(word.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            answer = False
            return answer
    return answer
    