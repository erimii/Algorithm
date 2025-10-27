# bj_7568 덩치

# 각 사람별로 자신보다 덩치 큰 사람 수 세기
# 큰 사람수 +1로 등수 저장

import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

ranks = []

for i in range(n):
  rank = 1
  for j in range(n):
    if i == j:
      continue
    if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
      rank+=1
      
  ranks.append(rank)

print(*ranks)

