k = int(input())
n = []

for i in range(k):
    num = int(input())
    if num == 0 :
        n.pop()
    else:
        n.append(num)

print(sum(n))
