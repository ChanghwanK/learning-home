N = int(input())

coordinate = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))

sorted_coordinate = sorted(coordinate, key=lambda x: (x[0], x[1]))


for x, y in sorted_coordinate:
    print(x, y)
