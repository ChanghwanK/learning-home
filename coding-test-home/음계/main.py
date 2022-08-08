# 음계
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# print("숫자를 입력")
input_value = list(map(int, input().split(' ')))

assending = True
descending = True

for i in range(1, len(input_value)):
    if input_value[i] < input_value[i - 1]:
        assending = False
    elif input_value[i] > input_value[i - 1]:
        descending = False

    
if assending:
    print("assending")
elif descending:
    print("descending")
else:
    print("mixed")