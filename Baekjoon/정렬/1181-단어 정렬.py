n = int(input())
l = []

for i in range(n):
    l.append(input())
    
l = list(set(l)) # 중복 제거 set
l.sort() # 정렬
l.sort(key=len) # 길이 정렬

for i in l:
    print(i)
