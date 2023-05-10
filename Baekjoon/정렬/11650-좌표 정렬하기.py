import sys
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    x, y = map(int,input().split())
    num.append([x, y])
num.sort()

for i in range(N):
    print(num[i][0],num[i][1])
    
    # sys 유무에 따라 시간 차이가 많이 남.
    # N번 x, y가 입력받는 과정 때문에 그런 듯.
