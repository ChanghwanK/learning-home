def solution(s):
    a = [int(word) for word in s.split(" ")]
    sorted_a = sorted(a)

    if sorted_a[0] < 0:
        answer = get_answer(sorted_a)
    else:
        answer = get_answer(sorted_a)

    return " ".join([str(num) for num in answer])


def get_answer(num_list):
    answers = list()
    answers.append(min(num_list))
    answers.append(max(num_list))
    return answers


# print(get_answer([-1, -2, -3, -4]))

print(solution("-1 -2 -3 -4"))