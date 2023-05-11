'''
문제
메이플스토리에는 전문 기술이라는 제작 시스템이 있다. 전문 기술은 특정량의 피로도가 쌓이는 대신 다양한 장비 및 비약을 제작할 수 있는 시스템이다. 
장신구 명장인 임스는 어떻게 하면 더 효율적으로 많은 장신구를 제작할 수 있을지 고민에 빠졌다.
임스가 만들 수 있는 장신구는 N개가 있고, 각각의 장신구를 만들면 Ai만큼의 피로도가 누적된다.
피로도가 200 미만인 경우, 장신구를 제작할 수 있다. 현재 쌓인 피로도가 P일 때, 임스가 제작할 수 있는 장신구의 최대 개수를 구해보자!

입력
첫 번째 줄에 정수 P와 정수 N이 공백으로 구분되어 주어진다. (1<=P<=200, 1<=N<=1000)
두 번째 줄에는 정수 A1,A2,...,AN 이 공백으로 구분되어 주어진다. (1<=Ai<=200)

출력
제작할 수 있는 장신구의 최대 개수를 출력하시오.
'''
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
