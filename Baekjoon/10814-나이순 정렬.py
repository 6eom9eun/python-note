import sys
input = sys.stdin.readline

N = int(input())
l = []
for i in range(N):
    [a, b] = map(str,input().split())
    l.append([a, b])

l.sort(key = lambda x : int(x[0])) # 이거 다시 확인하기.

for i in range(N):
    print(l[i][0], l[i][1])
