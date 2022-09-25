N = int(input())

infos = []
for _ in range(N):
    age, name = input().split()
    infos.append((int(age), name))

    infos.sort(key=lambda x: x[0])

