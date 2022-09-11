def solution(s):
    stack = list()

    for word in s:
        if word == "(":
            stack.append(word)
        elif word == ")":
            try:
                stack.pop()
            except IndexError:
                return False

    return True


result = solution("(())()")
print(result)