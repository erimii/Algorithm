# bj_1018 체스판 다시 칠하기

# 1. 8×8로 잘라볼 수 있는 모든 구간 탐색
# 2. 각 체스판에 대해 시작이 W인 경우와 B인 경우 비교해 더 적은 칸 수 선택 -> i+j%2==0->시작과 같은 색
# 3. 전체 중 최소값 출력

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def count_paint(x,y):
  start_w = 0
  start_b = 0
  for i in range(8):
    for j in range(8):
      current = board[x+i][y+j]
      if (i+j)%2 == 0:
        if current != 'W': start_w +=1
        if current != 'B': start_b +=1
      else:
        if current != 'B': start_w +=1
        if current != 'W': start_b +=1
  return min(start_w, start_b)

min_count=64
for i in range(n-7):
  for j in range(m-7):
    min_count = min(min_count, count_paint(i,j))

print(min_count)