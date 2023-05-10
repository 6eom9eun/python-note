N, M = map(int,input().split())
card = list(map(int,input().split()))
card_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                card_sum = max(card_sum, card[i]+card[j]+card[k])
                
print(card_sum)
