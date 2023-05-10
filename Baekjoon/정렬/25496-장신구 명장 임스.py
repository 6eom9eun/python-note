import sys
input = sys.stdin.readline

p, n = map(int,input().split())
a = list(map(int, input().split()))

a.sort()

count = 0

for i in a :
    p += i
    count += 1
    if p >= 200:
        break;

print(count)
# 오답임 다른 알고리즘 찾자
