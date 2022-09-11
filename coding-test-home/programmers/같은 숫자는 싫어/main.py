arr = [1, 1, 3, 3, 0, 1, 1]
arr_2 = [4, 4, 4, 3, 3]


def solution(arr):
    ## 순서 유지
    ## 연속 X
    ## 앞에들어간 숫자와 다음 턴 입력이 같은지 검사
    result = []

    for num in arr:
        # append
        input_num(result, num)

    answer = result

    return answer


def input_num(result, num):
    length = len(result)
    if length == 0:
        print(f"num {num}")
        result.append(num)
    else:
        data = result[-1]
        if data == num:
            pass
        else:
            result.append(num)


print(solution(arr_2))

if __name__ == "__main__":
    solution(arr)
