
def solution(s):
    answer = []
    start = (len(s) - 1)
    for i in range(start, -1, -1):
        answer.append(s[i])
    return answer

s = ["h","e","l","l","o"]
print(solution(s))