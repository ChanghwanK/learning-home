# ex 이름:=식

# before 3.8
a = [1, 2, 3, 4, 5]
n = len(a)

if n > 5:
    print(f"a list too long {n}")

# after 3.8
a = [1, 2, 3, 4, 5]

if (n := len(a)) > 5:
    print(f"a list too long {n}")


def solution(n):
    for i in range(3, 1000001):
        if n % i == 1:
            answer = i
            return answer


print(solution(12))


