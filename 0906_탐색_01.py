# 회문 문자열 검사

N = int(input())
s = []
for i in range(N):
  w = input()
  w = w.upper()
  s.append(w)

for idx, x in enumerate(s):
  if x == x[::-1]:
    print('#{} Yes'.format(idx+1))
  else:
    print('#{} No'.format(idx+1))