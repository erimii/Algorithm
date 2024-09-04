# 소수(에라토스테네스 체)
# 자연수 N이하의 소수 개수 출력

N = int(input())
s = [0]*(N+1)
cnt = 0

for i in range(2,N+1):
  if s[i] == 0:
    cnt +=1
    for j in range(i, N+1, i):
      s[j] = 1

print(cnt)