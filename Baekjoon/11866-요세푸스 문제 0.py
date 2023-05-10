import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
num = deque()

for i in range(1, N+1):
    num.append(i)

result = []

for i in range(N):
    num.rotate(-K+1)
    result.append(num[0])
    del num[0]

print("<",end='')
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")
