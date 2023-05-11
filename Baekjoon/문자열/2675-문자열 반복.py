n = int(input())

for _ in range(n):
    ns, s = input().split()
    for i in s:
        print(i*int(ns), end='')
    print()
