# bj_1475 방 번호

import sys
input = sys.stdin.readline

n = input().strip()
count = [0] * 10

for ch in n:
  count[int(ch)]+=1

count[6] = (count[6]+count[9])//2 + (count[6]+count[9])%2
count[9]=0
print(max(count))