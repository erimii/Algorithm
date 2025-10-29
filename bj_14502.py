# bj_14502 연구소
'''
연구소는 크기가 N×M인 직사각형
0은 빈 칸, 1은 벽, 2는 바이러스
벽의 개수는 3개
-> 안전 영역 크기의 최댓값
'''
'''
1. 0을 찾음
2. 3개의 빈칸 조합 선택
3. 바이러스퍼지게 함 -> def
4. 퍼진 후 0 개수 세기 -> def
5. 0 개수의 최대값 구하기
'''

import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus=[]
empty=[]
for i in range(n):
  for j in range(m):
    if lab[i][j] == 2:
      virus.append((i,j))
    elif lab[i][j] == 0:
      empty.append((i,j))

def spread_virus(temp):
  q = deque(virus)
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx, ny = x+dx[d], y+dy[d]
      if 0<=nx<n and 0<=ny<m:
        if temp[nx][ny] == 0:
          temp[nx][ny] = 2
          q.append((nx, ny))

def get_safe_area(temp):
  return sum(row.count(0) for row in temp)

max_safe=0

for wall in combinations(empty, 3):
  temp = copy.deepcopy(lab)
  for x,y in wall:
    temp[x][y] = 1
    
  spread_virus(temp)
  safe = get_safe_area(temp)
  max_safe = max(max_safe, safe)

print(max_safe)