# 주사위 게임

N = int(input())
re = []

for i in range(N):
  s = list(map(int, input().split()))
  s.sort()
  if s[0] == s[1]  == s[2]:
    re.append(10000 + s[0]*1000)
  elif s[0] == s[1] or s[1] == s[2]:
    re.append(1000 + s[1]*100)
  else:
    re.append(max(s)*100)

print(max(re))