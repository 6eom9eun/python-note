N = int(input())
A = set(map(int,input().split()))
M = int(input())
MA = list(map(int,input().split()))

for i in MA:
    if i in A:
        print(1)
    else:
        print(0)
