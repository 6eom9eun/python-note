import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []

for i in range(1, n+1):
    l.append(i)

tmp = 0

for _ in range(m):
    i, j = map(int,input().split())
    tmp = l[i-1]
    l[i-1] = l[j-1]
    l[j-1] = tmp

for i in l:
    print(i, end=' ')
