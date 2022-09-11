def solution(s):
    a = s.split(" ")
    new_str = list()

    for word in a:
        if is_first_word_upper(word):
            new_str.append(word)
        else:
            new_str.append(change_first_word_upper(word))

    return " ".join(new_str)


def is_first_word_upper(word):
    if word[0].isupper():
        return True
    return False


def change_first_word_upper(word):
    return word[0].upper() + word[1:].lower()


print(solution(" "))


def solution2(s):
    s = s.split(" ")

    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()

    return " ".join(s)

