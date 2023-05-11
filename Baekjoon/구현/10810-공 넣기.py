import sys
input = sys.stdin.readline

n, m = map(int, input().split())
b = [0] * n

for i in range(m):
    i, j, k = map(int,input().split())
    for _ in range(i-1, j):
        b[_] = k

for i in b:
    print(i, end=' ')
