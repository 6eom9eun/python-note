import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())

day = (V-B)/(A-B) # 유도하는게 쉽지 않음.
print(int(day) if day==int(day) else int(day)+1)

#for문을 이용해서 작성하면 시간초과뜸.

