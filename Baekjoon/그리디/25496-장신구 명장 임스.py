import sys
input = sys.stdin.readline

p, n = map(int,input().split())
a = list(map(int, input().split()))

a.sort()

count = 0

for i in a :
    if p < 200:
        p += i
        count += 1
    else:
        break;
        
print(count)
