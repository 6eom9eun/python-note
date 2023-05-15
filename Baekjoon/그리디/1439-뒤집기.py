S = input()

count = 0

for i in range(len(S)-1):
    if i != S[i+1]:
        count += 1

print((count+1)//2) 

# 0 or 1로 변환하면 되니까, 2로 나눈 몫.
# 0 -> 0 -> 0
# 0101 -> 3 -> 2
#010101 -> 5 -> 3
