N = int(input())
A = list(map(int,input().split()))
M = int(input())
MA = list(map(int,input().split()))

for i in MA:
    if i in A:
        print(1)
    else:
        print(0)
