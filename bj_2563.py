# bj_2563 색종이

# 100X100을 모두 흰색(0)으로 초기화
# 색종이 붙이는 부분만 검정색(1)으로 바꾸기


import sys
input = sys.stdin.readline

n = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j]=1

print(sum(sum(row) for row in paper))