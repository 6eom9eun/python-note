'''
문제
어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)
다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. 
dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.
이름이 같거나, 생일이 같은 사람은 없다.

출력
첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.
'''
import sys
input = sys.stdin.readline
n = int(input())
l = []

for _ in range(n):
    n,d,m,y = input().split()
    d,m,y = map(int,(d,m,y))    #숫자 데이터들을 int형으로 바꿈
    l.append((y,m,d,n))   #정렬을 위해서 년 월 일 순서로 배치해서 리스트에 삽입

l.sort()    #기본 올림차순으로, 낮은 연도가 l[0]로 오게 됨. 낮은 연도는 나이가 많은 것임.
print(l[-1][3])   #가장 어린 사람의 n (이름)
print(l[0][3])    #가장 늙은 사람의 n (이름)
