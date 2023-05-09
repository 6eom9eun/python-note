n, m = map(int,input().split())
if n == 0:
    print(0)
else:
    w = list(map(int,input().split()))

    box = 0
    count = 1
    for i in range(n-1, -1, -1):
        box += w[i]
        if box > m :
            count += 1
            box = w[i]
            
    print(count)
