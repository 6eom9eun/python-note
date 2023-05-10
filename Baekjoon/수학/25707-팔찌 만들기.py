n = int(input())
nl = list(map(int,input().split()))

nl.sort(reverse=True)

l = nl[0]

for i in range(n-1):
    l += nl[i]-nl[i+1]

l -= nl[n-1]
print(l)
