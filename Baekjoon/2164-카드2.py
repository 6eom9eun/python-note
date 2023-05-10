import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
card = deque()

for i in range(1,N+1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.rotate(-1)

print(card[0])

# deque 활용.
# 큐 관련 문제에서 활용할 수 있도록 기억해두자.
