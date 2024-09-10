# 카드 역배치

card = list(range(21))

def r_card(a, b, lst):
  for i in range((b-a+1)//2):
    lst[a+i], lst[b-i] = lst[b-i], lst[a+i]
  return lst
    
for _ in range(10):
  a, b = map(int,input().split())
  card=r_card(a, b, card)

for i in range(1,21):
  print(card[i], end=' ')