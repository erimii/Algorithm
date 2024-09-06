# 점수 계산

N = int(input())
s = list(map(int, input().split()))
score = 0
cnt = 0

for i in s:
  if i == 1:
    cnt += 1
    score += cnt
  else:
    cnt = 0

print(score)