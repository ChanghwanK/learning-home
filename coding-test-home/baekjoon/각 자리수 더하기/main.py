
N = int(input())

num_words = []

for _ in range(len(str(N))):
    num_words.append(N % 10)
    print("+++++++++")
    print(num_words)
    N = N//10
    print("+++++++++")
    print(N)


print(sum(num_words))
