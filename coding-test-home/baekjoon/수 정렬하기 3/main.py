N = int(input())

a = [0 for _ in range(N + 1)]

for i in range(N):
    num = int(input())
    a[num] += 1

print(a)
print("========")


for i in range(N + 1):
    for j in range(a[i]): # a[i] 만큼 index를 출력하는 것
        print(i)
