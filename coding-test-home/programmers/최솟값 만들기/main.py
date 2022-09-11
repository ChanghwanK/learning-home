def solution(A, B):
    answer = 0
    locks = []  # 한 번 사용한 친구들을 담음
    results = []
    # 한 번 사용한 것은 A, B 모두 lock에 넣기
    # 순차적으로 해보는 케이스
    # 순차적으로 하지 않는 케이스 등등이 존재함
    # 예를 들면 1,2 3,4 는 2*3 + 1*4 가 최소임
    # 따라서 한 사이클 돌면 다시 다른 경우의 수로 한 사이클 돌아야함
    for i in range(len(A)):
        for j in range(len(B)):
            results.append(result)
            if i not in locks:
                result = A[i] * B[j]
            else:
                continue
        #     locks.append(B[j])
        # locks.append(A[i])

    return answer

"""
어떻게 모든 경우의 수를 더 할 수 있지?
"""