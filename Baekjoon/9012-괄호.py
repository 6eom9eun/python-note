N = int(input())
a = []

for i in range(N):
    x, y = map(int, input().split())
    a.append([y,x])

b = sorted(a)

for i in range(N):
    print(b[i][1], b[i][0])
