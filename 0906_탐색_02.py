# 숫자만 추출

s = list(input())
sum = 0
cnt = 0

for x in s:
  if x.isdigit() == True:
    sum = sum*10 + int(x)

for i in range(1,sum+1):
  if sum % i == 0:
    cnt +=1

print(sum)
print(cnt)