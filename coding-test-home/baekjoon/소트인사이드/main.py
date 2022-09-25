"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

"""

"""
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

"""
N = input()
num_words = []


for num in N:
    num_words.append(num)

num_words.sort(reverse=True)

a = ''.join(num_words)

print(a)
