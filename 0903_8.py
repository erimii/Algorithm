# 뒤집은 소수
# N개의 자연수 뒤집었을때 소수이면 출려ㅕㄱ
# reverse(x), isPrime(x) 정의

def reverse(x):
  for i in str(x):
    re = 0
    cnt = 0
    for i in str(x):
      re += int(i)*10**(cnt)
      cnt +=1
  return re

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True
  
N = int(input())
n_list = list(map(int, input().split()))

for x in n_list:
  re_num = reverse(x)
  if isPrime(re_num):
    print(re_num, end = ' ')

